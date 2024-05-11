from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse



def welcome(request):
    return HttpResponse("Welcome to my Django App!")

urlpatterns = [
    path('api/posts/', include('apps.posts.urls')),
    path('api/category/', include('apps.category.urls')),
    path('admin/', admin.site.urls),
    path('', welcome),  # Ruta de bienvenida en la raíz del dominio
]
