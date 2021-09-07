from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from main.forms import JoinForm, LoginForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')


def login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request,user)
                    next = request.POST.get('next', 'home')
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'main/login.html', {"login_form": LoginForm() } )
    else:
        return render(request, 'main/login.html', { "login_form": LoginForm() })

@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return redirect("/")

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            print(join_form.errors)
            return render(request, 'main/join.html', { "join_form": join_form })
    else:
        return render(request, 'main/join.html', { "join_form": JoinForm() })
