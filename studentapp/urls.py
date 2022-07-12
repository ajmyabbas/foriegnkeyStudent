from unicodedata import name
from django import views
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('about/',views.about,name='about'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('logoutpage/',views.logoutpage,name="logoutpage"),
    path('addStudent',views.addStudent,name='addStudent'),
    path('student1',views.student1,name='student1'),
    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('course1',views.course1,name='course1'),
    path('add_course',views.add_course,name='add_course'),
    path('show_studentlist',views.show_studentlist,name='show_studentlist'),
]
