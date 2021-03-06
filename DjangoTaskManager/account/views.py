from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from DjangoTaskManager.account.forms import RegistrationForm


def account_login(request):
    """
    Purpose: Handles the creation of a new user for authentication

    Author: Max Baldridge

    Arguments: request -- the full HTTP request object

    Returns: n/a
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return HttpResponseRedirect(reverse('all_tasks'))
        else:
            return TemplateResponse(request, 'login.html', {'error': True})
    else:
        return TemplateResponse(request, 'login.html', {})


@login_required
def account_logout(request):
    """
    Purpose: Handles logging the user out from the system

    Author: max Baldridge

    Arguments: request -- the full hTTP response object

    Returns: n/a
    """
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the login.
    return HttpResponseRedirect(reverse('login'))


def account_register(request):
    """
    Purpose: Handles the creation of a new user for authentication

    Author: Max Baldridge

    Arguments: request -- the full HTTP response object

    Returns: n/a
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponseRedirect(reverse('all_tasks'))
        return TemplateResponse(
            request,
            'register.html',
            {'errors': form.errors})
    else:
        return TemplateResponse(request, 'register.html', {})
