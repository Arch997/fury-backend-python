from django.db import models
from django.contrib.auth.models import User

from planner.models import Event, Category

# Create your models here.


class Company(models.Model):
    """Model representing a company."""

    admin = models.CharField(max_length=200, null=True)
    events = models.ManyToManyField(Event)

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrator'

    def __str__(self):
        """Set a string representation of the object."""
        return self.admin


class Employee(models.Model):
    """Model representing an employee."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    todos = models.ManyToManyField(Event)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        """Set a string representation of the object."""
        return self.user


'''class Todo(models.Model):
	"""Represent the employee todo list."""
	user = models.ForeignKey(Employee, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	todos = models.ManyToManyField(Event)

	class Meta:
		verbose_name = "To-do List"
		'''


