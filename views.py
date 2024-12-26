import random
import string
from django.shortcuts import render

def gerar_senha(request):
  tamanho = request.GET.get('tamanho',12)
  tamanho = int(tamanho)
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  return render(request, 'senha/gerarador_de_senhas.html', {'senha':senha})
