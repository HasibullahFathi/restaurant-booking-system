from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile.

    Attributes:
        user (OneToOneField): The user associated with this profile.
        ROLE_CHOICES (tuple): Defines the available roles (Admin or Customer).
        role (IntegerField): The role of the user, defaulting to Customer.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = ((1, 'Admin'), (0, 'Customer'))
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.user.username


class Table(models.Model):
    """
    Represents a table in the restaurant.

    Attributes:
        table_number (IntegerField): A unique identifier for each table.
        capacity (IntegerField): The number of
        guests the table can accommodate.
        status (IntegerField): The current status of the
        table (Available, Reserved, or Cancelled).
    """
    TABLE_STATUS_CHOICES = [
        (1, 'Available'),
        (2, 'Reserved'),
        (0, 'Cancelled'),
    ]
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.IntegerField(choices=TABLE_STATUS_CHOICES, default=1)

    def __str__(self):
        return f"Table {self.table_number}"


class Shift(models.Model):
    """
    Represents a shift in the restaurant.

    Attributes:
        name (CharField): The name of the shift.
        start_time (TimeField): The start time of the shift.
        end_time (TimeField): The end time of the shift.
    """
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"


class Booking(models.Model):
    """
    Represents a booking made by a user.

    Attributes:
        user (ForeignKey): The user who made the booking.
        table (ForeignKey): The table that has been booked.
        phone_number (CharField): The phone number
        associated with the booking.
        booking_date (DateField): The date of the booking.
        booking_time (TimeField): The time of the booking.
        shift (ForeignKey): The shift during which the booking is made.
        created_on (DateTimeField): The timestamp when the booking was created.
        number_of_guests (IntegerField): The number of guests for the booking.
        status (IntegerField): The status of the
        booking (Confirmed, Cancelled, Available).
        remarks (TextField): Additional remarks or notes for the booking.

    Meta:
        ordering (list): Orders bookings by creation date in descending order.
        constraints (list): Enforces a unique constraint to ensure no
        duplicate bookings for the same table, date, shift, and status.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.IntegerField()
    STATUS_CHOICES = ((2, 'Confirmed'), (0, 'Cancelled'), (1, 'Available'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]
        constraints = [
            models.UniqueConstraint(

                fields=['table', 'booking_date', 'shift', 'status'],

                name='unique_booking_per_table_per_shift'

            )

        ]

    def __str__(self):
        return (
            f"Booking {self.id} by {self.user.username} "
            f"on {self.booking_date} at {self.booking_time}"
        )
