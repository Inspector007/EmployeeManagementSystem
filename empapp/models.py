# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse

class Employee(models.Model):
	empName = models.CharField(max_length = 50)
	empEmail = models.EmailField(max_length = 50)
	empPan = models.CharField(max_length = 50)

	def __str__(self):
		return self.empName

	def get_absolute_url(self):
		return reverse('empapp:employeedetail',args=[self.empName, self.empPan])


