from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.

def view_home(request):

	return render(request, 'base.html')



def student_list(request):
	student = StudentModel.objects.all()

	context = {
		'title' : 'Student List',
		'student' : student,
	}

	return render(request, 'student_list.html', context)



def add_student(request):

	if request.method == 'POST':
		name = request.POST.get('name')
		roll = request.POST.get('roll')
		department = request.POST.get('department')
		city = request.POST.get('city')
		profile_image = request.FILES.get('profile_image')

		StudentModel.objects.create(
				name = name,
				roll = roll,
				department = department,
				city = city,
				profile_image = profile_image
			)

		return redirect('student_list')

	context = {
		'title' : 'Add Student',
	}

	return render(request, 'add_student.html', context)



def delete_student(request, id):
	del_stu = StudentModel.objects.get(id=id)
	del_stu.delete()
	return redirect('student_list')



def edit_student(request, myid):

	student = StudentModel.objects.get(id=myid)

	if request.method == 'POST':
		student.name = request.POST.get('name')
		student.roll = request.POST.get('roll')
		student.department = request.POST.get('department')
		student.city = request.POST.get('city')
		student.profile_image = request.FILES.get('profile_image')
		student.save()

		return redirect('student_list')

	context = {
		'title' : 'Edit Student',
		'student' : student,
	}

	return render(request, 'edit_student.html', context)
