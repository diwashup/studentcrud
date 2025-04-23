from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("Student ID already exists.")
        return student_id
    def clean_student_email(self):
        student_email = self.cleaned_data.get('student_email')
        if Student.objects.filter(student_email=student_email).exists():
            raise forms.ValidationError("Student email already exists.")
        return student_email
    def clean_student_contact(self):
        student_contact = self.cleaned_data.get('student_contact')
        if Student.objects.filter(student_id=student_contact).exists():
            raise forms.ValidationError("Student contact already exists.")
        return student_contact
