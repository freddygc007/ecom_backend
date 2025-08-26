from django.shortcuts import render

# Create your views here.

def home(request):
    """Home page view"""
    return render(request, 'ecommerce/home.html')

def login(request):
    """Login page view"""
    return render(request, 'ecommerce/login.html')

def signup(request):
    """Signup page view"""
    return render(request, 'ecommerce/signup.html')

def products(request):
    """Products list page view"""
    return render(request, 'ecommerce/products.html')

def product_detail(request):
    """Product detail page view"""
    return render(request, 'ecommerce/product_detail.html')

def cart(request):
    """Shopping cart page view"""
    return render(request, 'ecommerce/cart.html')

def checkout(request):
    """Checkout page view"""
    return render(request, 'ecommerce/checkout.html')

def profile(request):
    """User profile page view"""
    return render(request, 'ecommerce/profile.html')
