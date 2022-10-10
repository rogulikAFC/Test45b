from django.shortcuts import render


def error404(request):
    return render(request, 'errors\\404.html')
