from django import forms
from .models import MenuCategory, MenuItem

class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name']

class MenuItemForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'min': '0'}), label="Price")
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'status', 'featured_image', 'category']


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price