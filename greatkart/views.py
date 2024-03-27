from django.shortcuts import render
from store.models import Product
def home(reqest):
    products = Product.objects.all().filter(is_available=True)
    context= {
        'products':products,
    }
    
    return render(reqest,"home.html",context)