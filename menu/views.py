from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MenuCategoryForm, MenuItemForm
from .models import MenuCategory, MenuItem


def menu_category_list(request):
    """
    View to display all menu categories with their related items.

    Retrieves all menu categories with their associated items 
    using prefetching and renders them in the 'menu/menu.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered menu page.
    """
    categories = MenuCategory.objects.prefetch_related(
        'menu_items').all()
    return render(
        request, 'menu/menu.html', {'categories': categories})


@login_required
def create_menu_category(request):
    """
    Handle the creation of a new menu category.

    Only staff users can create categories. If a category with the same name
    already exists, an error message is shown. If the form is valid and unique,
    the category is saved and a success message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to category list if successful,
                      or renders the category creation form.
    """
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to create a category")
        return redirect('menu_category_list')

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.cleaned_data['name']

            if MenuCategory.objects.filter(
                name__iexact=category_name
            ).exists():
                messages.error(
                    request, 
                    f"The category '{category_name}' already exists."
                )
            else:
                category_form.save()
                messages.success(
                    request, "The category has been successfully created.")
                return redirect('menu_category_list')

    else:
        category_form = MenuCategoryForm()

    context = {
        'category_form': category_form,
    }
    return render(request, 'menu/create_menu_category.html', context)


@login_required
def edit_menu_category(request, category_id):
    """
    Handle the editing of an existing menu category.

    Only staff users can edit categories. If a category with the new name
    already exists (excluding the current one), an error message is shown.
    If the form is valid and the new name is unique, the category is updated
    and a success message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.
        category_id (int): The ID of the category to edit.

    Returns:
        HttpResponse: Redirects to the category list if successful,
                      or renders the category edit form.
    """
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to edit categories.")
        return redirect('menu_category_list')

    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST, instance=category)

        if category_form.is_valid():
            new_name = category_form.cleaned_data['name']
            if MenuCategory.objects.filter(
                name=new_name
            ).exclude(id=category_id).exists():
                messages.error(
                    request, "A category with this name already exists."
                )
            else:
                category_form.save()
                messages.success(
                    request, "The category has been successfully updated.")
                return redirect('menu_category_list')
    else:
        category_form = MenuCategoryForm(instance=category)

    context = {
        'category_form': category_form,
        'category': category,
        'category_id': category_id,
    }
    return render(request, 'menu/create_menu_category.html', context)


@login_required
def delete_menu_category(request, category_id):
    """
    Handle the deletion of a menu category.

    Only staff users can delete categories. If the user is not authorized, 
    they are redirected to the category list. If the request method is POST, 
    the category is deleted, and a success message is shown.

    Args:
        request (HttpRequest): The HTTP request object.
        category_id (int): The ID of the category to be deleted.

    Returns:
        HttpResponse: Redirects to the category list after deletion or 
                      renders a confirmation page.
    """
    if not request.user.is_staff:
        return redirect('menu_category_list')

    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category.delete()
        messages.success(
            request, "The category has been successfully deleted.")
        return redirect('menu_category_list')

    context = {
        'category': category,
    }
    return render('menu_category_list')


@login_required
def create_menu_item(request):
    """
    Handle the creation of a new menu item.

    Only staff users can create menu items. If a menu item with the same name
    already exists, an error message is shown. If the form is valid and unique,
    the item is saved and a success message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the menu item creation form after success,
                      or renders the form for item creation.
    """
    if not request.user.is_staff:
        messages.error(
            request, "You are not authorized to create a menu item.")
        return redirect('menu_category_list')

    if request.method == 'POST':
        item_form = MenuItemForm(request.POST, request.FILES)

        if item_form.is_valid():
            item_name = item_form.cleaned_data['name']

            if MenuItem.objects.filter(name=item_name).exists():
                messages.error(
                    request, "A menu item with this name already exists.")
            else:
                item_form.save()
                messages.success(
                    request, "The menu item has been successfully created.")
                return redirect('menu_category_list')
    else:
        item_form = MenuItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request, 'menu/create_menu_item.html', context)


@login_required
def edit_menu_item(request, item_id):
    """
    Handle the editing of an existing menu item.

    Only staff users can edit menu items. If the form is valid and the new name
    is unique (excluding the current item), the item is updated and a success
    message is displayed. Otherwise, appropriate error messages are shown.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the menu item to be edited.

    Returns:
        HttpResponse: Redirects to the category list after successful update
                      or renders the edit form if the request is GET.
    """
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to edit a menu item.")
        return redirect('menu_category_list')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        item_form = MenuItemForm(
            request.POST, request.FILES, instance=menu_item)

        if item_form.is_valid():
            item_name = item_form.cleaned_data['name']

            if MenuItem.objects.filter(
                    name=item_name).exclude(id=item_id).exists():
                messages.error(
                        request, "A menu item with this name already exists.")
            else:
                item_form.save()
                messages.success(
                    request,
                    "The menu item has been successfully updated.")
                return redirect('menu_category_list')
    else:
        item_form = MenuItemForm(instance=menu_item)

    context = {
        'item_form': item_form,
        'menu_item': menu_item,
        'item_id': item_id,
    }
    return render(request, 'menu/create_menu_item.html', context)


@login_required
def delete_menu_item(request, item_id):
    """
    Handle the deletion of a menu item.

    Only staff users can delete menu items. If the user is not authorized,
    an error message is displayed and the user is redirected. If the item is
    found, it is deleted and a success message is shown.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the menu item to be deleted.

    Returns:
        HttpResponse: Redirects to the menu category list after deletion.
    """
    if not request.user.is_staff:
        messages.error(
            request, "You are not authorized to delete a menu item.")
        return redirect('menu_category_list')

    menu_item = get_object_or_404(MenuItem, id=item_id)

    menu_item.delete()
    messages.success(
            request,
            f"Menu item '{menu_item.name}' has been successfully deleted.")

    return redirect('menu_category_list')
