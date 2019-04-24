from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def products(request):
    return render(request, 'mainapp/catalog.html')


def feynmans_joke(request):
    return render(request, 'mainapp/products/feynmans_joke.html')


def harry_potter_01(request):
    return render(request, 'mainapp/products/harry_potter_01.html')


def star_massacres(request):
    return render(request, 'mainapp/products/star_massacres.html')
