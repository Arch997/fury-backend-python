from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.db import models

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from planner.models import Category, Event
from users.models import Company, Employee, Todo
from .forms import TodoForm, UserForm

# Create your views here.


"""def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='users:login'):
    '''Decorator for views that checks that the user is logged in and is a superuser.

    Redirecting to the login page if necessary.
    '''
    decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser, 
        login_url=login_url,
        redirect_field_name=redirect_field_name
        )
    if view_func:
        return decorator(view_func)
    return decorator"""


def index(request):
    """Landing page."""
    return render(request, 'planner/index.html')


@login_required
def events(request):
    """COmpany events view.

    These are events that are created by an admin and are not personal to an employee.
    Employee todos may be curated from these events.
    """
    '''events = Event.objects.filter(
        models.Q(events__category='Work')
        )'''
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'planner/events.html', context)


@login_required
def event(request, event_id):
    """Return a single event by id."""
    try:
        event = get_object_or_404(Event, id=event_id)
    except EventDoesNotExist:
        return Http404
        if event:
            desc = event.desc
            return HttpResponseRedirect(reverse('planner:event', args=['event_id']))
    context = {'event': event, 'desc': desc}
    return render(request, 'planner/event.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add(request, event_id):
    """Add a todo item."""
    new_event = Event.objects.all()  # Represents the company event list
    new_todo = Todo.objects.all()  # Represents the employee todo list
    if request.method == 'GET':
        form = TodoForm
    elif request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_event.save()  # When an event is added by admin, the admin events board increments
            new_todo.save()  # When an event is added by the admin, the employee's todo list increments
            return HttpResponseRedirect(reverse('planner:events'))
        else:
            messages.add_message(request, messages.error,
                                 'Submission Failed. Please try again')
    context = {'form': form}
    return render(request, 'planner/add_event.html', context)


@login_required
def todos(request):
    """Show all open todos."""
    todos = Todo.objects.filter(user=request.user).order_by('-time_added')
    context = {'todos': todos}
    return render(request, 'planner/todos.html', context)


@login_required
def todo(request, todo_id):
    """Show a single todo item."""
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.owner == request.user:
        return HttpResponseRedirect(reverse('planner:topic',
                                            args=[todo_id]))
    context = {'todo': todo}
    return render(request, 'planner/todo.html', context)









