from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinute, Event
from .forms import ResourceForm
# Create your views here.
def index(request):
    return render(request,'club/index.html')

def resourceslist (request):
    resource_list=Resource.objects.all()
    return render (request, 'club/resource.html', {'resource_list': resource_list})

def meetinglist (request):
    meeting_list=Meeting.objects.all()
    return render (request,'club/meeting.html',{'meeting_list':meeting_list})

def meetingdetail (request, id):
    detail=get_object_or_404(Meeting, pk=id)
    context={'detail':detail}
    return render (request,'club/detail.html',context=context)

    #form view
def newResource(request):
    form = ResourceForm()
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html',{'form': form})