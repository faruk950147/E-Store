from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(never_cache, name='dispatch')
class HomeView(View):
    def get(self, request):
        messages.success(request, 'Welcome to our store!')
        return render(request, 'store/home.html')
    
class ProductView(View):
    def get(self, request):
        messages.success(request, 'Product details page loaded!')
        return render(request, 'store/product-detail.html')

