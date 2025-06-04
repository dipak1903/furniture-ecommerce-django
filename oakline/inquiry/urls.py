from django.urls import path 
from inquiry.views import *

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
