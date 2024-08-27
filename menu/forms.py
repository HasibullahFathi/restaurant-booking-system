from django import forms
from .models import MenuCategory, MenuItem

# Form for MenuCategory
class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name']

# Form for MenuItem
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'status']
