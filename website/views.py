from django.shortcuts import render, get_object_or_404

from .models import Item, Category
# Create your views here.

def index(request):
    return render(request, 'website/index.html', {
        'items': Item.objects.all(),
        'categories': Category.objects.all()
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    sameBrandItems = Item.objects.filter(brand=item.brand, is_sold=False).exclude(brand='Unknown').exclude(pk=pk)
    similarItems = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

    return render(request, 'website/detail.html', {
        'item': item,
        'similarItems': similarItems
    })