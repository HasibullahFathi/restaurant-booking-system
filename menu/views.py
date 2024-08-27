from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import MenuCategory, MenuItem
# from .forms import MenuCategoryForm, MenuItemForm
from django.contrib import messages

# Check if the user is admin
def is_admin(user):
    return user.is_superuser  # Or check user.profile.role == 1 if using a role system

# View for creating menu category (admin only)
@login_required
@user_passes_test(is_admin)
def create_menu_category(request):
    if request.method == 'POST':
        form = MenuCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu Category created successfully.")
            return redirect('menu_category_list')  # Adjust this URL to where you list categories
    else:
        form = MenuCategoryForm()

    return render(request, 'menu/create_menu_category.html', {'form': form})

# View for creating menu item (admin only)
@login_required
@user_passes_test(is_admin)
def create_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu Item created successfully.")
            return redirect('menu_item_list')  # Adjust this URL to where you list menu items
    else:
        form = MenuItemForm()

    return render(request, 'menu/create_menu_item.html', {'form': form})


# View to list all menu categories

def menu_category_list(request):
    categories = MenuCategory.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})

# View to show details of a specific menu item
def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu/menu_item_detail.html', {'item': item})
