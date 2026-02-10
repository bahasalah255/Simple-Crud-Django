from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student
from .forms import *
# Create your views here.
def student_list(request):
    context = {
        "pro": Student.objects.all(),

    }
    return render(request,'students/student.html',context)
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('student_list')
           
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})
def editform(request,pk):
    student = Student.objects.get(id=pk)
    form = None
    if request.method == 'POST':
            form = StudentForm(request.POST,instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
    else :
            form = StudentForm(instance=student)
    return render(request,'students/edit.html',{'form' : form})
def delete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student_list')
    return render(request,'students/student.html')
