from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1= request.POST['password']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password1']
        if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,"Username Taken")
               return redirect('register')
           elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id Taken")
                return redirect ('register')
           else:
               user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                        password=password1)
               user.save()
               return redirect('login')
        else:
           messages.info(request, "password not matching")
           return redirect('register')
        return redirect('/')
    return render(request, "registration.html")



def logout(request):
    auth.logout(request)
    return redirect('/')