# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from users.models import Employee, Todo, Event


class TodoForm(forms.ModelForm):
    """Form for receiving the todo items."""

    class Meta:
        model = Event
        fields = ['title', 'desc']
        labels = {'text': _('Todo'),
                  }

        widgets = {'title': forms.Textarea(), 'desc': forms.Textarea()}
        help_texts = {'text': _('Your todo title'),
                      'desc': _('A description of your todo item')
                      }
        error_messages = {
            'text': {
                'max_length': _('Title cannot be empty'),
                },
            }


class UserForm(forms.ModelForm):
    """Custom form for login and registration implementation."""

    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('department', 'position')
    


'''class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category     
        CHOICES = (('work', 'Work'), ('personal', 'Personal'))
        field = forms.ChoiceField(choices=CHOICES)'''
