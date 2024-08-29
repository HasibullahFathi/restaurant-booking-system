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
        messages.error(request, "You are not authorized to create a category")
        return redirect('menu_category_list')  # Redirect to a page that handles unauthorized access

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.cleaned_data['name']  # Assuming 'name' is the field in your form

            if MenuCategory.objects.filter(name__iexact=category_name).exists():
                messages.error(request, f"The category '{category_name}' already exists.")
            else:
                category_form.save()
                messages.success(request, "The category has been successfully created.")
                return redirect('menu_category_list')

    else:
        category_form = MenuCategoryForm()

    context = {
        'category_form': category_form,
    }
    return render(request, 'menu/create_menu_category.html', context)


@login_required
def edit_menu_category(request, category_id):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to edit categories.")
        return redirect('menu_category_list')  # Redirect to a page that handles unauthorized access

    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category_form = MenuCategoryForm(request.POST, instance=category)
        
        if category_form.is_valid():
            new_name = category_form.cleaned_data['name']
            if MenuCategory.objects.filter(name=new_name).exclude(id=category_id).exists():
                messages.error(request, "A category with this name already exists.")
            else:
                category_form.save()
                messages.success(request, "The category has been successfully updated.")
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
    if not request.user.is_staff:
        return redirect('menu_category_list')

    category = get_object_or_404(MenuCategory, id=category_id)

    if request.method == 'POST':
        category.delete()
        messages.success(request, "The category has been successfully deleted.")
        return redirect('menu_category_list')

    context = {
        'category': category,
    }
    return render('menu_category_list')


@login_required
def create_menu_item(request):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to create a menu item.")
        return redirect('menu_category_list')

    if request.method == 'POST':
        item_form = MenuItemForm(request.POST, request.FILES)
        
        if item_form.is_valid():
            item_name = item_form.cleaned_data['name']
            
            if MenuItem.objects.filter(name=item_name).exists():
                messages.error(request, "A menu item with this name already exists.")
            else:
                item_form.save()
                messages.success(request, "The menu item has been successfully created.")
                return redirect('create_menu_item')
    else:
        item_form = MenuItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request, 'menu/create_menu_item.html', context)


from django.shortcuts import get_object_or_404, redirect, render
from .forms import MenuItemForm
from .models import MenuItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def edit_menu_item(request, item_id):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to edit a menu item.")
        return redirect('menu_category_list')

    # Fetch the menu item or return a 404 if not found
    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        item_form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        
        if item_form.is_valid():
            item_name = item_form.cleaned_data['name']
            
            # Check if another item with the same name exists (exclude the current item)
            if MenuItem.objects.filter(name=item_name).exclude(id=item_id).exists():
                messages.error(request, "A menu item with this name already exists.")
            else:
                item_form.save()
                messages.success(request, "The menu item has been successfully updated.")
                return redirect('menu_category_list')
    else:
        item_form = MenuItemForm(instance=menu_item)

    context = {
        'item_form': item_form,
        'menu_item': menu_item,
        'item_id': item_id,
    }
    return render(request, 'menu/create_menu_item.html', context)





