from django import forms
from .models import Resource, Meeting, MeetingMinute, Event

class ResourceForm (forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'