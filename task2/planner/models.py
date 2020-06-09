from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """Category for events."""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Set string representation of the object."""
        return self.name


class Event(models.Model):
    """Create a todo model."""

    title = models.CharField(max_length=200)
    desc = models.TextField(verbose_name='description', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=False)
    # sowner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Event')
        verbose_name_plural = 'Events'
        ordering = ['-created']  # Ordering by oldest event

    def __str__(self):
        """Set string representation of the object."""
        return self.title


'''class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todos = models.ManyToManyField(Todo, on_delete=models.CASCADE)'''
