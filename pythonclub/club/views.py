from django.shortcuts import render
from .models import Resource, Meeting, MeetingMinute, Event
# Create your views here.
def index(request):
    return render(request,'club/index.html')

def resourceslist (request):
    resource_list=Resource.objects.all()
    return render (request, 'club/resource.html', {'resource_list': resource_list})
