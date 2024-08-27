from django.db import models

# MenuCategory Model
class MenuCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# MenuItem Model
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    FOOD_STATUS = ((1, 'Available'), (0, 'Not Available'))
    status = models.IntegerField(choices=FOOD_STATUS, default=1)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name