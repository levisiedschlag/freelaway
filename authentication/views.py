from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        if not password == confirm_password:
            return redirect('/auth/cadastro')
        
        if len(password.strip()) < 8 or len(username.strip()) < 8:
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)
        if user.exists():
            return redirect('/auth/cadastro')
        try:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            return redirect('auth/login')

        except:
            return redirect('auth/cadastro')
            

        


def login(request):
    return HttpResponse('<h1>Login</h1>')