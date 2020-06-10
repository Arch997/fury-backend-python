# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from users.models import Employee, Event


class TodoForm(forms.ModelForm):
    """Form for receiving the todo items."""

    class Meta:
        model = Event
        fields = ['title', 'desc', 'category', 'due_date']
        labels = {'text': _('Todo'),
                  }

        widgets = {'title': forms.TextInput(), 'desc': forms.Textarea(),
        'category': forms.Select()}
        help_texts = {'text': _('Your todo title'),
                      'desc': _('A description of your event item'),
                      'category': _('What category does this event belong to'),
                      'due_date': _("Time of Event"),
                      }
        error_messages = {
            'title': {
                'max_length': _('Title cannot be empty'),
                },
            }


class SignUpForm(forms.ModelForm):
    """Custom form for login and registration implementation."""

    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department', 'position')
    

