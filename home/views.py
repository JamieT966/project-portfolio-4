from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return render(request, 'index.html')