# service/forms.py
from django import forms
from .models import ServiceRequest, Comment

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
