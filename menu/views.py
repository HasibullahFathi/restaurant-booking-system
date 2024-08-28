from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MenuCategory, MenuItem
from .forms import MenuCategoryForm, MenuItemForm
from django.contrib import messages

def menu_category_list(request):
    categories = MenuCategory.objects.prefetch_related('menu_items').all()
    return render(request, 'menu/menu.html', {'categories': categories})


@login_required
def create_menu_and_category(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('menu_category_list')

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST)
        item_form = MenuItemForm(request.POST, request.FILES)

        if category_form.is_valid() and 'category_submit' in request.POST:
            category_form.save()
            messages.success(request, "Category created successfully!")
            return redirect('create_menu')

        if item_form.is_valid() and 'item_submit' in request.POST:
            item_form.save()
            messages.success(request, "Menu item created successfully!")
            return redirect('create_menu')

        if not category_form.is_valid():
            messages.error(request, "There was an error creating the category. Please check the form.")
        if not item_form.is_valid():
            messages.error(request, "There was an error creating the menu item. Please check the form.")
    
    else:
        category_form = MenuCategoryForm()
        item_form = MenuItemForm()

    context = {
        'category_form': category_form,
        'item_form': item_form,
    }
    return render(request, 'menu/create_menu_item.html', context)

