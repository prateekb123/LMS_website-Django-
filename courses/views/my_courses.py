from django.shortcuts import render
from courses.models import UserCourse, Course
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url = "login_page")
def Mycourses(request):
    user_courses = UserCourse.objects.filter(user = request.user)
    return render(request, "courses/my_courses.html", {"user_courses":user_courses})
