from re import A
from django.contrib import admin
from studentapp.models import Student
from studentapp.models import course

# Register your models here.
@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ('id','std_name','std_address','std_age','std_email','joining_date')


@admin.register(course)
class courseadmin(admin.ModelAdmin):
    list_display = ('id','course_name','fee')