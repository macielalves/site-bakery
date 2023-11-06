from django.urls import path
from . import views


app_name = ''

urlpatterns = [
    path('catalogo/<int:id_>/', views.catalogo, name="catalogo"),
    path('', views.main, name="home"),
    path('welcome/', views.hello, name="welcome")
]
