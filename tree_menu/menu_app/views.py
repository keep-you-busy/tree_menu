from django.shortcuts import render


def index(request, menu_name):
    context = {
        'menu_name': menu_name,
    }
    return render(request, 'menu/index.html', context)
