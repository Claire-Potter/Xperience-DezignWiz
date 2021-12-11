"""
Xperiencedezignwiz home app views configuration

the index view is setup to display the homepage.
the social media views are setup to authorise login via the
various social media apps. This was completed as per the django
documentation:
https://django-rest-auth.readthedocs.io/en/latest/installation.html
"""

from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter)
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from .models import Home, Verification
from .forms import EmailForm


def index(request):
    """ A view to return the index page """
    home = Home

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)


def verification(request):
    """ A view to return the google verification page """
    verification_id = (Verification.objects
                       .filter(verification="google50b8ec44e2d448c8.html")
                       .latest())

    context = {
        'verification_id': verification_id,
    }

    return render(request, 'google50b8ec44e2d448c8.html', context)


class FacebookLogin(SocialLoginView):
    """ A view to authorise login via Facebook """
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """ A view to authorise login via Twitter """
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


def send_email(request):

    # create a variable to keep track of the form
    message_sent = False
    recipient_list = ""

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            c_d = form.cleaned_data
            subject = c_d['subject']
            text_content = c_d['message']
            recipient_list = c_d['recipients']

            # send the email to the recipent
            msg = EmailMultiAlternatives(from_email=settings.DEFAULT_FROM_EMAIL,
                                         reply_to=['xperiencedezignwiz@gmail.com'],
                                         to=['xperiencedezignwiz@gmail.com'],
                                         bcc=recipient_list,
                                         subject=subject,
                                         body=text_content)
            msg.template_id = "d-9430602ecd0f411f8caa22367da72cbd"
            msg.dynamic_template_data = {"message": text_content, "subject": subject}
            msg.send(fail_silently=False)

            # set the variable initially created to True
            message_sent = True

    else:
        form = EmailForm()

    return render(request, 'email.html', {

        'form': form,
        'message_sent': message_sent,
        'recipient_list': recipient_list,

    })
