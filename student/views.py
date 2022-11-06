from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html',{'students': students})


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_number = form.cleaned_data['student_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            field_of_study = form.cleaned_data['field_of_study']
            gpa = form.cleaned_data['gpa']

            new_student = Student(student_number=student_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            field_of_study=field_of_study,
            gpa=gpa
            )

            new_student.save()

            return redirect('index')
    else:
        form = StudentForm()
        return render(request, 'students/add.html', {'form': form})


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {'form': form})
    

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))