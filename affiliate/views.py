from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def rex(request):
    return render(request, 't1.html', {})
