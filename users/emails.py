from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(user):
    subject = 'Welcome to SynthAIze'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    context = {'user': user}
    html_message = render_to_string('emails/welcome_email.html', context)
    
    email = EmailMessage(subject, html_message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send(fail_silently=False)