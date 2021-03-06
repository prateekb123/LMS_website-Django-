from django.shortcuts import render, redirect
from courses.models import Course, Video, UserCourse
from django.shortcuts import HttpResponse

def coursePage(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')

    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number = serial_number, course = course)

    if video.is_preview is False:

        if (request.user.is_authenticated is False):
            return redirect('login_page')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user, course = course)
            
            except:
                return redirect('checkout_page', slug = course.slug)
    
    context = {
        'course': course,
        'video':  video
    }
    return render(request, "courses/courses_page.html", context = context)