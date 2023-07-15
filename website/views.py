from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse
from django.db.models import Q

from .models import Item, Category
from .forms import addItemForm
# Create your views here.

def index(request):
    items = Item.objects.all().exclude(created_by=request.user)
    categories = Category.objects.all()
    query = request.GET.get('query', '')
    category = request.GET.get('category', '0')
    title = 'Explore all Products: '

    if category != '0':
        items = items.filter(category=category)
        title = 'Filter Results:'

    elif query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        title = 'Search Results:'
        if items == None:
            title = 'No Product Found! '

    return render(request, 'website/index.html', {
        'items': items,
        'categories': categories,
        'title': title,
        'ctg': int(category)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    sameBrandItems = Item.objects.filter(brand=item.brand, is_sold=False).exclude(brand='Unknown').exclude(pk=pk)
    similarItems = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

    return render(request, 'website/detail.html', {
        'item': item,
        'similarItems': similarItems
    })

def add(request):
    if request.method=='POST':
        form = addItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    
    else: 
        form = addItemForm()

    return render(request, 'website/add.html',{
        'form': form
    })
