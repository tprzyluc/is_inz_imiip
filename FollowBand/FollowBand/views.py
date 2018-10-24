from django.shortcuts import render

def start(request):
    return render(request,'start.html')

def mainpage(request):
    return render(request, 'mainpage.html')
    