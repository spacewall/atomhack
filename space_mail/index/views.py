from django.shortcuts import render

def index(request):
    template = 'navigate.html'

    return render(request, template)
