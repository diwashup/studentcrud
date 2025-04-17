from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('list')
    else:
        form= StudentForm()
    return render(request, 'create.html', {'form': form})

def list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

def update(request, id):
    student = get_object_or_404(Student, student_id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    student = get_object_or_404(Student, student_id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, 'delete.html', {'student': student})

