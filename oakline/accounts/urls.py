from django.urls import path
from accounts.views import RegisterView, CustomLoginView, CustomLogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user-profile/', ProfileView.as_view(), name='profile'),
]
