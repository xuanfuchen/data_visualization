from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'html/test.html')

def macro(request):
    data = []
    return render(request, 'html/test.html')