from django.shortcuts import render


# Create your views here.

def index(request):
    """Delcaração de função de view"""
    return render(request, 'index.html')
