from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    ROLE_CHOICES = [('1', 'Admin'), ('0', 'Customer')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='0')

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
    STATUS_CHOICES = [('1', 'Confirmed'), ('0', 'Cancelled')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"