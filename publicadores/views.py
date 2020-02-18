from django.shortcuts import render

def index(request):
    context = {
        'titulo':'Menu'
    }
    return render(request, 'index.html', context=context)
