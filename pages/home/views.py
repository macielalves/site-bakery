from django.shortcuts import render


def main(request):
    teste = 'Isso é um teste'
    return render(
        request,
        'index.html',
        {
            'text': teste
        }
    )
