from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect

from website.models import Item
from website.forms import editItemForm
# Create your views here.

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dashboard.html', {
        'items': items
    })

def edit(request, pk):
    if request.method=='POST':
        item = Item.objects.get(pk=pk)
        form = editItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detail', pk)
    else:
        item = Item.objects.get(pk=pk)
        form = editItemForm(instance=item)

    return render(request, 'dashboard/edit.html', {
        'form': form,
        'item': item
    })

def deleteItem(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('dashboard')