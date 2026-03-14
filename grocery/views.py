from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GroceryItem
from .forms import GroceryItemForm


def index(request):
    """Display all grocery items and handle edit mode"""
    items = GroceryItem.objects.all()
    edit_id = request.GET.get('edit')
    edit_item = None
    form = None

    if edit_id:
        edit_item = get_object_or_404(GroceryItem, id=edit_id)
        form = GroceryItemForm(instance=edit_item)
    else:
        form = GroceryItemForm()

    context = {
        'items': items,
        'edit_item': edit_item,
        'form': form,
    }
    return render(request, 'grocery/index.html', context)


def add_item(request):
    """Add a new grocery item"""
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Added Successfully!')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f'{field}: {", ".join(errors)}')

    return redirect('grocery:index')


def update_item(request, item_id):
    """Update an existing grocery item"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        form = GroceryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Updated Successfully!')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f'{field}: {", ".join(errors)}')

    return redirect('grocery:index')


def toggle_completed(request, item_id):
    """Toggle the completed status of a grocery item"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.completed = not item.completed
        item.save()
    return redirect('grocery:index')


def delete_item(request, item_id):
    """Delete a grocery item"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()
        messages.success(request, 'Item Deleted Successfully!')
    return redirect('grocery:index')


def edit_item(request, item_id):
    """Redirect to index with edit parameter"""
    from django.urls import reverse
    return redirect(f"{reverse('grocery:index')}?edit={item_id}")
