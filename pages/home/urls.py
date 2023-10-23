from django.urls import path
from . import views


app_name = ''

urlpatterns = [
    path('', views.main, name="home"),
    path('catalogo/<int:id>/', views.catalogo, name="catalogo"),
    path('welcome/', views.hello, name="welcome")
]
