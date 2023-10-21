# home
from django.shortcuts import render


def main(request):
    context = {
        'texto': 'Site Bakery'
    }

    return render(
        request,
        'legal/index.html',
        context
    )
