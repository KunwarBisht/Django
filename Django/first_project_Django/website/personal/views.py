from django.shortcuts import render

def index(request):
    return render(request ,'personal2/home.html')

def contact(request):
    return render(request,'personal2/basic.html',{'content':['if you would like to contact me','kunwarsingh@gmail.com']})
