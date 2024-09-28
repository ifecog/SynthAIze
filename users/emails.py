from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from users.tokens import account_activation_token


def send_welcome_email(request, user):
    subject = 'Welcome to SynthAIze'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    # Activation
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    
    current_site = get_current_site(request)
    domain = f"{request.scheme}://{current_site.domain}"
    activation_link = f"{domain}{reverse('activate-account', kwargs={'uidb64': uid, 'token': token})}"
    
    context = {'user': user, 'activation_link': activation_link}
    html_message = render_to_string('emails/welcome_email.html', context)
    
    email = EmailMessage(subject, html_message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send(fail_silently=False)