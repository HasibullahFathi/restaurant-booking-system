from django.db import models
from cloudinary.models import CloudinaryField


# MenuCategory Model
class MenuCategory(models.Model):
    """
    Model representing a category of menu items.

    This model holds the name of the category, which can be used to
    group related menu items together.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# MenuItem Model
class MenuItem(models.Model):
    """
    Model representing an item on the menu.

    This model contains information about a specific menu item,
    including its name, description, price, availability status,
    featured image, and associated category.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    FOOD_STATUS = ((1, 'Available'), (0, 'Not Available'))
    status = models.IntegerField(choices=FOOD_STATUS, default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name
