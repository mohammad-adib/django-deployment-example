from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app_one/index.html')

def other(request):
    return render(request,'app_one/other.html')

def relative(request):
    return render(request,'app_one/relative.html')
