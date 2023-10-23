from django.shortcuts import render


def main(request):
    a = [x for x in range(3)]
    print(a)
    titulo = f"Site Bakery"
    context = {
        "title": titulo,
        "alt": "Folder 1",
        "lista": a
    }
    return render(request, "index.html", context)


def catalogo(request, id):
    print("Catalogo de Pagina Web:", id)
    context = {
        'title': "Site Bakery",
        'id': id
    }
    return render(request, "catalogo.html", context)


def hello(request):
    return render(
            request,
            "hello.html",
        )
