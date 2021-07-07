from django.contrib import admin
from courses.models import Course, Tag, Learning, Prerequisite, Video, UserCourse, Payment
from django.utils.html import format_html


class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]
    list_display = ['name', 'price', 'discount', 'active']


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['order_id', 'get_user', 'get_course', 'status']
    list_filter = ['status', 'course']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")

    def get_course(self, payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = 'Course'
    get_user.short_description = 'User'


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment, PaymentAdmin )
admin.site.register(UserCourse)
