from django.shortcuts import render


def main(request):
    teste = 'Isso é um teste'
    titulo = f'{__name__}'
    context = {
        'text': teste,
        'title': titulo
    }
    return render(
        request,
        'index.html',
        context
    )
