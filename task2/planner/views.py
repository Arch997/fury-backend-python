from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.db import models

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import DeleteView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from planner.models import Category, Event
from users.models import Company, Employee
from .forms import TodoForm, SignUpForm

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
    event = Event.objects.get(id=event_id)
    descriptor = event.desc
    context = {'event': event, 'descriptor': descriptor}
    return render(request, 'planner/event.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add(request):
    """Add a todo item.

    @user_passes_test decorator ensures only an administrator can add event.
    """
    # TODO: Update the Employee todo field with new events as appropriate. 
    # Possibly check if the task scheduler API can interface with the /
    # users.todo view to alert the user(Employee) to new events in their departments(category)

    if request.method == 'GET':
        form = TodoForm()
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.save()  # When an event is added by admin, the admin events board increments
            
            return HttpResponseRedirect(reverse('planner:events'))
        else:
            messages.add_message(request, messages.error,
                                 'Submission Failed. Please try again')
    context = {'form': form}
    return render(request, 'planner/add_event.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit(request, event_id):
    """Edit an event"""
    event = Event.objects.get(id=event_id)
    if request.method == 'GET':
        """Pre-fill the form with the existing entry."""
        form = TodoForm(instance=event)
    elif request.method == "POST":
        """ POST data submitted; process data."""
        form = TodoForm(instance=event, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('planner:event', 
                args=[event.id]))

    context = {'form': form, 'event': event}
    return render(request, 'planner/edit_event.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete(request, event_id):
    """Delete an event."""
    event = Event.objects.get(id=event_id)
    
    event.delete()
    messages.success(request, "Event deleted")
    return HttpResponseRedirect(reverse('planner:events'))
    
    context = {'event': event}
    return render(request, 'planner/delete_event.html', context)
