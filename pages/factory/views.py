from django.shortcuts import render
from django.http import HttpResponse

# Classe de exemplo para usuários
class User:
    def __init__(self):
        self.__status = False
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
    return HttpResponse('Voçê ainda não é usuário! <a href="/login">Fazer Cadastro</a>')
