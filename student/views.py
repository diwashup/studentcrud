from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages


def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Student created successfully') 
            return redirect('list')
        else:
            messages.error(request, 'please fill form properly')
    else:
        form= StudentForm()
    return render(request, 'create.html', {'form': form})

def list(request):
    query= request.GET.get('q')
    print("Query:", query)
    if query:
        students = Student.objects.filter(
            Q(student_name__icontains=query) | 
            Q(student_id__icontains=query))
    else:
        students = Student.objects.all()
    paginator = Paginator(students, 5)  # Show 10 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
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

