from django.db import models

# Create your models here.
class StudentModel(models.Model):

	name = models.CharField(max_length=100, null=True)
	roll = models.CharField(max_length=20, null=True)
	department = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=250, null=True)
	profile_image = models.ImageField(upload_to="students/", null=True,blank=True)

	def __str__(self):
		return self.name
