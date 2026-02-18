from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {
        "name":"ravi",
        "reg":"125033"
    }
    return render(request,'index.html', context=data)