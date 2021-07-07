from django.shortcuts import render, redirect
from courses.models import Course
from django.shortcuts import HttpResponse
from courses.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import logout


class Signup(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, "courses/signup.html", {'form':form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("login_page")
        return render(request, "courses/signup.html", {'form':form})
        
    

class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "courses/login.html", {'form':form})

    def post(self, request):
        form = LoginForm(request = request, data = request.POST)
        if form.is_valid():
            next_page = self.request.GET.get('next')
            if next_page is not None:
                return redirect(next_page)

            return redirect("home")
        return render(request, "courses/login.html", {'form':form})


def Logout(request):
    logout(request)
    return redirect("home")
