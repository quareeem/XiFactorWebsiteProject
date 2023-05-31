from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib import messages
from django_ratelimit.decorators import ratelimit

from .forms import PersonToContactForm


def home(request, *args, **kwargs):
    return render(request, 'index.html')

def e(request, *args, **kwargs):
    return render(request, 'example.html')

def about(request, *args, **kwargs):
    return render(request, 'about.html')

def services(request, *args, **kwargs):
    return render(request, 'services.html')

def sector(request, *args, **kwargs):
    return render(request, 'sector.html')

def portfolio(request, *args, **kwargs):
    return render(request, 'portfolio.html')

def solutions(request, *args, **kwargs):
    return render(request, 'solutions.html')

def research(request, *args, **kwargs):
    return render(request, 'research.html')

def success(request, *args, **kwargs):
    return render(request, 'success.html')


@require_http_methods(["GET", "POST"])
# @ratelimit(key='user_or_ip', rate='10/m')
def contacts(request, *args, **kwargs):
    if request.method == 'POST':
        form = PersonToContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added successfully!')
            return redirect('success')
        else:
            messages.error(request, 'Form is not valid')
    else:
        messages.get_messages(request).used = True
    return render(request, 'contacts.html')