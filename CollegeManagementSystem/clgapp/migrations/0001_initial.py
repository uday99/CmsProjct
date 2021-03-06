# Generated by Django 3.1.7 on 2021-08-13 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeModel',
            fields=[
                ('cname', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('c_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('d_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.collegemodel')),
            ],
        ),
        migrations.CreateModel(
            name='LecturerModel',
            fields=[
                ('lecturer_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('l_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.collegemodel')),
                ('depname', models.ManyToManyField(to='clgapp.DepartmentModel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('s_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.collegemodel')),
                ('dep', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clgapp.departmentmodel')),
                ('lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.lecturermodel')),
            ],
        ),
    ]
