from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'calculator/index.html', {'items': items})
