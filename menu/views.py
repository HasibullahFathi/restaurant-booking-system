from django.shortcuts import render, get_object_or_404
from .models import MenuCategory, MenuItem

# View to list all menu categories

def menu_category_list(request):
    categories = MenuCategory.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})

# View to show details of a specific menu item
def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu/menu_item_detail.html', {'item': item})
