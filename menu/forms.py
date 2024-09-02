from django import forms
from .models import MenuCategory, MenuItem

from django import forms
from .models import MenuCategory, MenuItem

class MenuCategoryForm(forms.ModelForm):
    """
    Form for creating and updating `MenuCategory` instances.

    This form handles the creation and updating of menu categories,
    allowing the user to input the name of the category.
    """
    class Meta:
        model = MenuCategory
        fields = ['name']


class MenuItemForm(forms.ModelForm):
    """
    Form for creating and updating `MenuItem` instances.

    This form allows the user to create or update menu items by
    providing fields for the name, description, price, status,
    featured image, and category. It includes validation to ensure
    that the price is a positive value.
    """
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        label="Price"
    )
    
    class Meta:
        model = MenuItem
        fields = [
            'name', 'description', 'price', 
            'status', 'featured_image', 'category'
        ]

    def clean_price(self):
        """
        Validates the price field to ensure it is greater than zero.

        Returns:
            int: The validated price.

        Raises:
            forms.ValidationError: If the price is zero or negative.
        """
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError(
                "Price must be greater than zero."
            )
        return price
