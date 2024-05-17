from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from rest_framework import generics, status
from rest_framework.response import Response 
from .serializers import StudentSerializer
from rest_framework.views import APIView

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        Student.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk" 

def hello(request):
    return render(request, 'baowebapp/test.html')

def main(request):
    students = Student.objects.all()
    return render(request, 'baowebapp/main.html', {'students':students})

def addMember(request):
    form = StudentForm()
    context = {'form':form}

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        school = request.POST.get('school')

        Student.objects.create(name=name, gender=gender, school=school)
        return render(request, 'baowebapp/main.html')
    return render(request, 'baowebapp/add_member.html', context)

def updateMember(request, pk):
    student = Student.objects.get(student_id=pk)
    form = StudentForm(instance=student)

    context = {'form':form}

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('main')

    return render(request, 'baowebapp/add_member.html', context)

def deleteMember(request, pk):
    student = Student.objects.get(student_id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('main')
    return render(request, 'baowebapp/delete_member.html', {'student':student})

