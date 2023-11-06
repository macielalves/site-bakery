from django.shortcuts import render, redirect


def main(request):
    a = [
        0,
        1,
        2,
    ]
    titulo = f"Site Bakery"
    context = {
        "title": titulo,
        "alt": "Folder 1",
        "lista": a
    }
    return render(request, "index.html", context)


def catalogo(request, id_):
    print("Catalogo de Pagina Web:", id_)
    context = {
        'title': "Site Bakery",
        'id_': id_
    }
    if id_ != -1:
        return render(request, "catalogo.html", context)
    return redirect('home')


def hello(request):
    return render(
            request,
            "hello.html",
        )
