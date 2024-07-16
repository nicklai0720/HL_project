from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.utils.timezone import now
from django.db.models import Sum
import calendar


def home(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    
    items = Item.objects.all()
    return render(request, 'inventory/home.html', {'items': items, 'form': form})

def manage(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        new_stock = request.POST.get('new_stock')
        item = get_object_or_404(Item, id=item_id)
        item.current_stock = new_stock
        item.save()
        return redirect('manage')
    
    items = Item.objects.all()
    return render(request, 'inventory/manage.html', {'items': items})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('manage')

def chart(request):
    data = {}
    items = Item.objects.all()
    for item in items:
        data[item.name] = [item.current_stock]
    return render(request, 'inventory/chart.html', {'data': data})

