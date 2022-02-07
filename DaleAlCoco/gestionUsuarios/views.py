from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from gestionUsuarios.forms import UserForm, SignupForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
    
def register(request):
    
  
    name = request.POST.get('username')
    passwordreg = request.POST.get('password')
    password2 = request.POST.get('password2')
    user_form = SignupForm(request.POST)
    user = authenticate(username=name, password=passwordreg)
        
        
    
    return render(request,"register.html",{'user_form': user_form})
    
    