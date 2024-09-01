from datetime import datetime, time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Booking, Profile, Shift, Table
from .forms import BookingForm


class BookingList(LoginRequiredMixin, ListView):
    """
    View to list bookings for the logged-in user.

    - Displays all bookings if the user's profile role is 1 (admin).
    - Displays only the user's bookings if the profile role is not 1.
    - Bookings are paginated, with 8 entries per page.
    - The context includes the current page number.
    """

    model = Booking
    template_name = 'booking/booking.html'
    context_object_name = 'bookings'
    paginate_by = 8

    def get_queryset(self):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist for the user.")

        if profile.role == 1:
            return Booking.objects.all().order_by(
                "-booking_date", "-created_on")
        else:
            return Booking.objects.filter(user=self.request.user).order_by(
                "-booking_date", "-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page', 1)
        return context


class BookingDetail(DetailView):
    """
    View to display detailed information about a specific booking.

    - Uses the 'Booking' model.
    - Renders the 'booking/booking_detail.html' template.
    - The booking object is accessed via the 'booking' context variable.
    """
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking'


def index(request):
    """
    Render the index page for the booking app.

    - Renders the 'booking/index.html' template.
    - Accepts the HTTP request object as a parameter.
    """
    return render(request, 'booking/index.html')


@login_required
def create_booking(request):
    """
    Handle the creation of a new booking.

    - If the request method is POST:
        - Validate the submitted booking form.
        - Ensure the booking date is in the future.
        - Check that the booking time is within the
        selected shift's time range.
        - Verify that the selected table is available.
        - Ensure no existing booking conflicts with
        the same table, date, and shift.
        - Save the booking if all checks pass and redirect to the booking list.
        - Display appropriate error messages if any checks fail.
    - If the request method is not POST:
        - Display an empty booking form.

    Returns:
        - Renders the booking form template with the form context.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            selected_shift = booking.shift
            booking_time = booking.booking_time

            if booking.booking_date < timezone.now().date():
                messages.error(
                    request, "Booking date must be in the future."
                )
                return render(
                    request, 'booking/booking_form.html', {'form': form}
                )

            if not (
                selected_shift.start_time <= booking_time <=
                selected_shift.end_time
            ):
                msg = (
                    f"Booking time must be between "
                    f"{selected_shift.start_time} "
                    f"and {selected_shift.end_time} "
                    f"for the {selected_shift.name} shift."
                )
                messages.error(request, msg)
                return render(
                    request, 'booking/booking_form.html', {'form': form}
                )

            if booking.table.status != 1:
                messages.error(
                    request, "The selected table is not available."
                )
                return render(
                    request, 'booking/booking_form.html', {'form': form}
                )

            if Booking.objects.filter(
                table=booking.table,
                booking_date=booking.booking_date,
                shift=booking.shift
            ).exists():
                messages.error(
                    request, "This table is already booked at this time."

                )
                return render(
                    request, 'booking/booking_form.html', {'form': form}
                )

            booking.save()
            messages.success(
                request, "Your booking has been successfully created!"
            )
            return redirect('booking_list')

        else:
            messages.error(request, "There was an error with your booking.")
            return render(
                request, 'booking/booking_form.html', {'form': form}
            )

    else:
        form = BookingForm()

    return render(
        request, 'booking/booking_form.html', {'form': form}
    )


@login_required
def edit_booking(request, booking_id):
    """
    Handle the editing of an existing booking.

    - Retrieves the booking with the given `booking_id`,
    or raises a 404 if not found.
    - Displays the current booking details in the form for editing.

    - If the request method is POST:
        - Validates and processes the form data.
        - Ensures the booking date is in the future.
        - Checks that the booking time falls within the
        selected shift's time range.
        - Verifies that the table is not already booked
        for the same date and shift.
        - Updates the booking if all checks pass and
        redirects to the booking list.
        - Displays error messages if any checks fail.

    - If the request method is not POST:
        - Displays the form pre-filled with the current booking details.

    Returns:
        - Renders the booking form template with the form,
        tables, and booking ID as context.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    tables = Table.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.user = request.user
            selected_shift = updated_booking.shift
            booking_time = updated_booking.booking_time

            # Check if the booking date is in the future
            if updated_booking.booking_date < timezone.now().date():
                messages.error(request, "Booking date must be in the future.")
                return render(
                    request, 'booking/booking_form.html', {
                        'form': form,
                        'tables': tables,
                        'booking_id': booking_id
                    })

            # Check if the booking time falls within the selected shift
            if not (selected_shift.start_time <=
                    booking_time <= selected_shift.end_time):
                messages.error(
                    request,
                    f"Booking time must be between {selected_shift.start_time}"
                    f" and {selected_shift.end_time} "
                    f"for the {selected_shift.name} shift.")
                return render(request, 'booking/booking_form.html', {
                    'form': form,
                    'tables': tables,
                    'booking_id': booking_id
                    }
                )

            # Check for existing bookings for the
            # same table on the same date and shift
            if Booking.objects.filter(
                table=updated_booking.table,
                booking_date=updated_booking.booking_date,
                shift=updated_booking.shift
            ).exclude(id=booking.id).exists():
                messages.error(
                    request,
                    "This table is already booked at the selected shift.")
                return render(request, 'booking/booking_form.html', {
                    'form': form,
                    'tables': tables,
                    'booking_id': booking_id
                })

            updated_booking.save()

            messages.success(
                request,
                "Your booking has been successfully updated!")
            return redirect('booking_list')

        else:
            messages.error(request, "There was an error with your booking.")
            return render(request, 'booking/booking_form.html', {
                'form': form,
                'tables': tables,
                'booking_id': booking_id
            })

    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/booking_form.html', {
        'form': form,
        'tables': tables,
        'booking_id': booking_id
    })


@login_required
def delete_booking(request, booking_id):
    """
    Handle the deletion of an existing booking.

    - Retrieves the booking with the given `booking_id`,
    or raises a 404 if not found.
    - Updates the status of the associated table to available (status = 1).
    - Deletes the booking from the database.
    - Displays a success message upon successful deletion.
    - Redirects the user to the booking list page.

    Returns:
        - Redirects to the booking list after the booking is deleted.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    table = booking.table
    table.status = 1
    table.save()

    booking.delete()

    messages.success(request, "The booking has been successfully deleted.")
    return redirect('booking_list')
