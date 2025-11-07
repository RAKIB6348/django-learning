from django.urls import path
from myapp.views import *

urlpatterns = [
	path('', view_home, name='home'),
	path('student-list/', student_list, name='student_list'),
	path('student-add/', add_student, name="add_student"),
	path('student-delete/<int:id>/', delete_student, name="delete_student"),
	path('student-edit/<int:myid>/', edit_student, name="edit_student"),
]