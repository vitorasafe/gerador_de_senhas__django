from django.urls import path
from .views import gerar_senha

urlpatterns = [
    path('gerar/', gerar_senha, name='gerar_senha'),
]
