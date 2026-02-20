from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import lengthPageView
from .views import searchEmpPageView
from .views import findEmpPageView
            
urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/<str:trip_name>/<int:trip_length>", aboutPageView, name="about"),
    path("length/<int:trip_length>", lengthPageView, name="length"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"),    
    ]                  