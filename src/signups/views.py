from django.shortcuts import render
from .models import SignUp

# Create your views here.

def home(request):
    signups = SignUp.objects.order_by('timestamp')
    return render(request, "signup.html", {'signup': signups})