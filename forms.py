# from django.core import validators
# from django import forms
# from .models import DailyReport

# class EmployeeReport():
#     class Meta:
#         models = DailyReport
#         fields = ["name", "email", "Assigned Work", "Completed","Pending"]
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.EmailInput(attrs={'class':'form-control'}),
#             'Assigned Work': forms.TextInput(attrs={'class':'form-control'}),
#             'Completed': forms.TextInput(attrs={'class':'form-control'}),
#             'Pending': forms.TextInput(attrs={'class':'form-control'}),
#         }

from django import forms
from .models import DailyReport

class EmployeeReport(forms.ModelForm):  
    class Meta:
        model = DailyReport
        fields = ["name", "email", "assigned_work", "completed", "pending"]  # Make sure field names match your model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'assigned_work': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.TextInput(attrs={'class': 'form-control'}),
            'pending': forms.TextInput(attrs={'class': 'form-control'}),
        }