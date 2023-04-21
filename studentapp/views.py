from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.

def stud_details(request):
    if request.method == 'POST':
        a = studentform(request.POST)
        if a.is_valid():
            sn = a.cleaned_data['student_name']
            dob = a.cleaned_data['dateofbirth']
            ph = a.cleaned_data['physics']
            ch = a.cleaned_data['chemistry']
            ma = a.cleaned_data['maths']
            cs = a.cleaned_data['computerscience']
            marks = [ph, ch, ma, cs]

            for i in marks:
                if i < 0 or i > 100:
                    return HttpResponse("Enter a Mark Between 0 - 100")

            total_marks = sum(marks)
            percentage = (total_marks / 400) * 100
            pc = percentage

            b = studentmodel(student_name=sn, dateofbirth=dob, physics=ph, chemistry=ch, maths=ma,
                             computerscience=cs, percentage=pc)
            b.save()
            return HttpResponse("Student Details Uploaded Successfully")

        else:
            return HttpResponse("Enter Valid Details")
    else:
        return render(request, 'stud_details.html')



def stud_display(request):
    a = studentmodel.objects.all()
    return render(request, 'stud_display.html', {'a': a})