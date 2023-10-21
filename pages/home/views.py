from django.shortcuts import render


def main(request):
    teste = "Hello 01"
    body = "Hello"
    titulo = f"{__name__}"
    context = {"text": teste, "title": titulo, "body": body}
    return render(request, "index.html", context)
