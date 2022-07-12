from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from studentapp.models import Student, course


# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')        

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')    
    
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login')
    else:
        return render(request,'signup.html')

#User login functionality view
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Welcome {username}')
			return redirect('about')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		#messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')

#User logout functionality view
@login_required(login_url='login')
def logoutpage(request):
    return render(request,'logout.html')
@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('home')

@login_required(login_url='login')
def addStudent(request):
    return render(request,'student.html')

@login_required(login_url='login')
def add_student_details(request):
    if request.method=='POST':
        sname=request.POST['student_name']
        saddress=request.POST['address']
        sage=request.POST['age']
        semail=request.POST['email']
        sjd=request.POST['joining_date']
        sel1=request.POST['sel']
        course1=course.objects.get(id=sel1)

        student=Student(std_name=sname,
                               std_address=saddress,
                               std_age=sage,
                               std_email=semail,
                               joining_date=sjd,
                               course=course1
                               )
        student.save()
        print("hii")
        return redirect('show_studentlist')

@login_required(login_url='login')
def show_studentlist(request):
    students=Student.objects.all()
    courses=course.objects.all()
    con={
        'students':students,
        'courses':courses
    }
    return render(request,'showstudents.html',con)

@login_required(login_url='login')
def course1(request):
    return render(request,'course.html')

@login_required(login_url='login')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html',context)



@login_required(login_url='login')  
def add_course(request): 
    if request.method=='POST':
        cors=request.POST['cors']
        cfee=request.POST['cfee']
        crs=course() 
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        return redirect(student1)     