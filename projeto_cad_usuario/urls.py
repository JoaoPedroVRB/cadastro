from django.contrib import admin
from django.urls import path
from app_cad_usuarios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('usuarios/', usuarios, name='listagem_usuarios' )
]
