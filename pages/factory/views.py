from django.shortcuts import render, redirect, loader
from django.http import HttpResponse


# Classe de exemplo para usuários
class User:
    def __init__(self):
        self.__status = True
        pass

    @property
    def logado(self):
        return self.__status


def main(request):
    user = User()
    if user.logado:
        return render(
            request,
            'factory/index.html'
        )
    teste = 'Warning'
    titulo = f'{__name__}'
    context = {
        'text': teste,
        'title': titulo
    }
    # return HttpResponse('Voçê ainda não é usuário! <a href="/login">Fazer Cadastro</a>')
    return redirect('home')
