from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.

def indexPageView(request):
    return render(request, 'travelpages/index.html')

def aboutPageView(request, trip_name, trip_length):
    context = {
                "trip_name" : trip_name,
                "trip_length" : trip_length + 2,
                "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
            }
    return render(request, 'travelpages/about.html', context)

def lengthPageView(request, trip_length):
    true_length = trip_length * 2
    info = {"trip_length":true_length}
    return render(request, 'travelpages/length.html', info)

def findEmpPageView(request) :
                return render(request, 'searchEmps.html')
            
def searchEmpPageView(request) :
    sFirst = request.GET.get('first_name', '')
    sLast = request.GET.get('last_name', '')
    
    data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)

    if data.count() > 0:
        context = {
            "our_emps" : data
        }
        return render(request, 'homepages/displayEmps.html', context)
    else:
        return HttpResponse("Not found")