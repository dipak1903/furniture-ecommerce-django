from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from catalog.models import Product
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class ProductsView(View):
    def get(self, request):
        category = request.GET.get('category')
        if category and category != 'All':
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        return render(request, 'products.html', {'products': products, 'selected_category': category or 'All'})


