from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', ProductsView.as_view(), name='catalog'),
]
