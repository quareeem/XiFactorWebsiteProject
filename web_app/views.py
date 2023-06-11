from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib import messages
from django_ratelimit.decorators import ratelimit
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext, get_language_info

from web_app.utils import send_contact_notification_email

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

def solutions_arxiv(request, *args, **kwargs):
    return render(request, 'solutions_arxiv.html')

def solutions_sebes(request, *args, **kwargs):
    return render(request, 'solutions_sebes.html')

def research(request, *args, **kwargs):
    trans_str = translate(language='ru')
    return render(request, 'research.html', {'trans_str': trans_str})

def success(request, *args, **kwargs):
    return render(request, 'success.html')


@require_http_methods(["GET", "POST"])
# @ratelimit(key='user_or_ip', rate='10/m')
def contacts(request, *args, **kwargs):
    if request.method == 'POST':
        form = PersonToContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_contact_notification_email(name=request.POST['name'], email=request.POST['email'])
            except:
                raise EOFError('SOME PROBLEM SNEIDNG EMAL')
            messages.success(request, 'Contact added successfully!')
            return redirect('success')
        else:
            messages.error(request, 'Form is not valid')
    else:
        messages.get_messages(request).used = True
    return render(request, 'contacts.html')


def translate(language):
    current_lang = get_language()
    try:
        print(get_language_info(get_language()))
        activate(language)
        print(get_language_info(get_language()))
        text = _('Hello')
        print('- - SUCCESSFULL - -')
    finally:
        activate(current_lang)
    return text