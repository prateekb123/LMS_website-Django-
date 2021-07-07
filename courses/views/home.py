from django.shortcuts import render
from courses.models import Course
from django.shortcuts import HttpResponse

def Home(request):
    courses = Course.objects.all()
    return render(request, "courses/home.html", {'courses':courses})
