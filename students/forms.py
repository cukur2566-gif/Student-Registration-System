from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'university_id',
            'id_number',
            'mobile_number',
            'address',
            'date_of_birth',
            'image'
        ]

        labels = {
            'name': 'Full Name',
            'university_id': 'University ID',
            'id_number': 'ID Number',
            'mobile_number': 'Mobile Number',
            'address': 'Address',
            'date_of_birth': 'Date of Birth',
            'image': 'Student Image'
        }

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }