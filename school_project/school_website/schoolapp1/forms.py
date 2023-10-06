
from django import forms
from .models import Department, Course

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'age-field'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('NoteBook', 'Notebook'), ('Textbook', 'Textbook'), ('ExamPapers', 'Exam Papers'),('Stationery','Stationery')],
        widget=forms.CheckboxSelectMultiple()
    )
