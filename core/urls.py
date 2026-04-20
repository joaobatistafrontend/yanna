from django.urls import path,include
from .views import home,singup
urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', singup, name='singup'),
    path("accounts/", include("django.contrib.auth.urls")),
]