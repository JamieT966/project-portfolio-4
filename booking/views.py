from django.shortcuts import render
from django.http import HttpResponse

def booking_page_view(request):
    return render(request, 'booking.html')