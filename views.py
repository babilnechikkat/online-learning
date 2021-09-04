from django.http.response import HttpResponse
from .models import *
from django.http import request
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            data={
                'name':name,
                'email':email,
                'subject':subject,
                'message':message,
            
            }
            # print(data)
            message='''
            New message:{}
            from:{}
            '''.format(data['message'],data['email'])
            send_mail(data['subject'],message,'',['babilkodakkad123@gmail.com'])
            # return HttpResponse("SEND")
        return render(request,"contact.html")

def courses(request):
   return render(request,"courses.html")

def trainers(request):
    return render(request,"trainers.html")

def events(request):
    return render(request,"events.html")

def coursedetails(request):
    return render(request,"course-details.html")

def termsandcontition(request):
    return render(request,"termsandcontition.html")


def login(request):
    msg=""
    if request.method=='POST':
            username2=request.POST.get('username2')
            password2=request.POST.get('password2')
            if logi.objects.filter(username2=username2,password2=password2):
                data=regi.objects.get(username=username2,password=password2)
                request.session['userid']=data.id
                if data.status=='admin':
                    return render(request,"register.html",{'msg':msg})
                elif data.status=='1':
                    return render(request,"meeting.html",{'msg':msg})    
            else:
                msg="incorrect password or username"
    return render(request,"login.html",{'msg':msg})

# 


def register(request):
    msg=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        contact=request.POST.get("phone")
        if password==confirmpassword:
            data=regi.objects.create(username=name,email=email,password=password,phone=contact,status=1)
            data=logi.objects.create(username2=name,password2=password,status=1)
            msg="registration succesfully done"
            return render(request,'login.html',{'msg':msg})
        else:
            msg="password doesnot match"
    return render(request,'register.html',{'msg':msg})




# def first(request):
#     return render(request,'useapp/hello.html')

def meeting(request):
    
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            data={
                'name':name,
                'email':email,
                'subject':subject,
                'message':message,
            
            }
            # print(data)
            message='''
            New message:{}
            from:{}
            '''.format(data['message'],data['email'])
            send_mail(data['subject'],message,'',['babilkodakkad123@gmail.com'])
        return render(request,"meeting.html")

def djangoevent(request):
    return render(request,"djangoevent.html")

def cybers(request):
    return render(request,"cybers.html")

def android(request):
    return render(request,"android.html")