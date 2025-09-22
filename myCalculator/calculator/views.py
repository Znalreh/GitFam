from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all().order_by('-created_at')  # Fetch all items
    context = {
        'app_name': 'Calculator App',  # Dynamic app name
        'items': items                 # Items from database
    }
    return render(request, 'calculator/index.html', context)
