from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = ((1, 'Admin'), (0, 'Customer'))
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.user.username


# 2. Table Model
class Table(models.Model):
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
    name = models.CharField(max_length=100)  # Example: "Morning Shift", "Evening Shift"
    start_time = models.TimeField()  # Example: 10:00 AM
    end_time = models.TimeField()    # Example: 02:00 PM

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"

# 3. Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who makes the booking
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True) 
    booking_date = models.DateField()
    booking_time = models.TimeField()
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)  # Reference to Shift
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
        return f"Booking {self.id} by {self.user.username} on {self.booking_date} at {self.booking_time}"
    
