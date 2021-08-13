from django.shortcuts import render
from .models import *
# Create your views here.
def studentApp(request):
    if request.method == 'POST':
        sname=request.POST.get('s1')


        sm=StudentModel.objects.filter(s_name__icontains=sname)
        return render(request, "student.html", {'sm': sm})
    else:
        return render(request,"student.html")


def lectApp(request):
    if request.method == 'POST':
        name=request._post.get('n1')
        print(name)


        lm=LecturerModel.objects.filter(l_name=name)
        print(lm.values())

        
        dm=DepartmentModel.objects.filter(lecturermodel__l_name=name)
        print(dm)


        return render(request, "lecturer.html",{'lm':lm,'dm':dm})
    else:
        return render(request,"lecturer.html")


    # lm=LecturerModel.objects.filter()
    # print(lm.lecturer_id)


def depApp(request):
    if request.method=='POST':
        dname=request.POST.get('d1')
        print(dname)
        sm=StudentModel.objects.filter(dep=DepartmentModel.objects.get(dep_name=dname))
        print("Student")
        print(sm.values())
        lm=LecturerModel.objects.filter(depname=DepartmentModel.objects.get(dep_name=dname))
        print('lecturers')
        print(lm.values())



        return render(request,"department.html",{'sm':sm,'lm':lm})
    else:
        return render(request, "department.html")