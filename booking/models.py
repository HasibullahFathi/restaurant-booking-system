from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    ROLE_CHOICES = ((1, 'Admin'), (0, 'Customer'))
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.user.username


# 2. Table Model
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"


# 3. Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who makes the booking
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # The table being booked
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.IntegerField()
    STATUS_CHOICES = ((1, 'Confirmed'), (0, 'Cancelled'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]
        constraints = [
            models.UniqueConstraint(
                fields=['table', 'booking_date', 'booking_time', 'status'],
                name='unique_booking_per_table_per_time'
            )
        ]

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    def clean(self):
        # Check if a booking already exists for this table, date, and time
        conflicting_bookings = Booking.objects.filter(
            table=self.table,
            booking_date=self.booking_date,
            booking_time=self.booking_time,
            status=1
        ).exclude(id=self.id)
        
        if conflicting_bookings.exists():
            raise ValidationError("This table is already booked for the selected date and time.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method to validate
        super().save(*args, **kwargs)
    
