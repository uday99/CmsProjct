# CmsProjct
CollegeManagementSystem

This project uses Django Relationships
one to one
one to many
many to many


how to run project
====================

python manage.py makemigrations
python manage.py migrate


create superuser to store the details different models:
=======================================================
collegemodel
DepartmentModel
lecturerModel
StudentModel


urls:
http://127.0.0.1:8000/     ----- to search and display student details using student name 
http://127.0.0.1:8000/lect ------ to search and display lecturer details using lecturer name and displays departments
http://127.0.0.1:8000/dep/  -------to search student and lecturer details using departmentName

