from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MenuCategory, MenuItem
from .forms import MenuCategoryForm, MenuItemForm
from django.contrib import messages


def menu_category_list(request):
    categories = MenuCategory.objects.prefetch_related('menu_items').all()
    return render(request, 'menu/menu.html', {'categories': categories})


@login_required
def create_menu_category(request):
    if not request.user.is_staff:
        return redirect('menu_category_list')  # Redirect to a page that handles unauthorized access

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('create_menu_category')  # Redirect to the same page or another page after saving
    else:
        category_form = MenuCategoryForm()

    context = {
        'category_form': category_form,
    }
    return render(request, 'menu/create_menu_category.html', context)

@login_required
def create_menu_item(request):
    if not request.user.is_staff:
        return redirect('menu_category_list')  # Redirect to a page that handles unauthorized access

    if request.method == 'POST':
        item_form = MenuItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save()
            return redirect('create_menu_item')  # Redirect to the same page or another page after saving
    else:
        item_form = MenuItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request, 'menu/create_menu_item.html', context)


@login_required
def edit_menu_category(request, category_id):
    if not request.user.is_staff:
        return redirect('menu_category_list')  # Redirect to a page that handles unauthorized access

    # Fetch the category or return a 404 if not found
    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('menu_category_list')  # Redirect to a list or detail page after saving
    else:
        category_form = MenuCategoryForm(instance=category)

    context = {
        'category_form': category_form,
        'category': category,
    }
    return render(request, 'menu/edit_menu_category.html', context)


@login_required
def delete_menu_category(request, category_id):
    if not request.user.is_staff:
        return redirect('menu_category_list')  # Redirect if the user is not an admin

    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('menu_category_list')  # Redirect after successful deletion

    context = {
        'category': category,
    }
    return render('menu_category_list')