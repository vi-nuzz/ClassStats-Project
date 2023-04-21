from django import forms

class studentform(forms.Form):
    student_name = forms.CharField(max_length=30)
    dateofbirth = forms.DateField()
    physics = forms.IntegerField()
    chemistry = forms.IntegerField()
    maths = forms.IntegerField()
    computerscience = forms.IntegerField()
