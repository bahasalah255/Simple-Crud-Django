# forms.py
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age' , 'email']  # أي field بغيت من model
