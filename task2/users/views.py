from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from planner.forms import TodoForm, UserForm, UserProfileForm

# Create your views here.


def register(request):
    """Register a user."""
    if request.method == 'GET':
        user_form = UserForm()
        profile_form = UserProfileForm()
    elif request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            profile_form.save()
            auth_employee = authenticate(username=new_user.username,
                                password=request.POST['password'])
            login(request, auth_employee)

            return HttpResponseRedirect(reverse('planner:add'))

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


@login_required
def logout_view(request):
    """Handle logout."""
    logout(request)
    return HttpResponseRedirect(reverse('planner:index'))


#def admin_login(request):
