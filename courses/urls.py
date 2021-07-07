from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from courses.views import Home, coursePage, Signup, Logout, Login, checkout, verify_payment, Mycourses


urlpatterns = [
    path('', Home , name = "home"),
    path('course/<str:slug>', coursePage , name = "course_page"),
    path('signup', Signup.as_view() , name = "signup_page"),
    path('checkout/<str:slug>', checkout , name = "checkout_page"),
    path('login', Login.as_view() , name = "login_page"),
    path('logout', Logout , name = "logout_page"),
    path('verify_payment', verify_payment , name = "verify_payment"),
    path('my-courses', Mycourses , name = "my-courses")
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)