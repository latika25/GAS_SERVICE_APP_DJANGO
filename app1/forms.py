from django.forms import ModelForm

from app1.models import ServiceRequest
class ServiceRequestForm(ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details','attachment'
                  ]