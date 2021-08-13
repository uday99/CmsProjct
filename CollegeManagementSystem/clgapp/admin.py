from django.contrib import admin

from .models import *


admin.site.register(CollegeModel)

@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['d_no','clg','dep_name']

#admin.site.register(DepartmentModel)
admin.site.register(LecturerModel)

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','s_name','email','lname','clg','dep']



#admin.site.register(StudentModel)

# Register your models here.
