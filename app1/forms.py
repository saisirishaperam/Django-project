from django import forms

from app1.models import student,teacher

class st_form(forms.ModelForm):
    
    class Meta:
        model = student
        fields = '__all__'

class teach_form(forms.ModelForm):
    
    class Meta:
        model = teacher
        fields = '__all__'