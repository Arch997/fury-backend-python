from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from planner.forms import TodoForm, SignUpForm, UserProfileForm

# Create your views here.


def register(request):
    """Register a user."""
    # TODO: Possibly refactor the the Employee model to allow for registration as it is currently unavailable
    if request.method == 'GET':
        form = UserCreationForm()
        profile_form = UserProfileForm()
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            a_user = form.save(commit=False)
            a_user.id = request.user.id
            a_user.save()
            profile_form.save()
            raw_password = form.cleaned_data.get('password1')
            auth_employee = authenticate(username=a_user.username,
                                password=raw_password)
            login(request, auth_employee)

            return HttpResponseRedirect(reverse('planner:add_event'))

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


@login_required
def logout_view(request):
    """Handle logout."""
    logout(request)
    return HttpResponseRedirect(reverse('planner:index'))


@login_required
def todos(request):
	"""List out employee todo items according to their department."""
	employee = Employee.objects.get(user=request.user)
	department = employee.department
	todos = Events.objects.filter(category=department)
	context = {'todos': todos}
	return render(request, 'users/todos.html', context)


@login_required
def todo(request, todo_id):
	"""A single todo item."""
	# TODO: Write view an add URL


def clear_todo(request, todo_id):
	"""Clear a todo item if due date-time is reached."""
	# TODO: Write view.


