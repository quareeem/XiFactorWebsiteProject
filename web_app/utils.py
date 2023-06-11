from django.core.mail import send_mail
from django.conf import settings


def send_contact_notification_email(name, email):
    subject = 'New Contact Form Submission'
    message = f'Hi Admin,\n\nA new contact form has been submitted.\n\nName: {name}\nEmail: {email}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
