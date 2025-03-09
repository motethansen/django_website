from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    """Home page view accessible to all users."""
    return render(request, 'home.html', {})
