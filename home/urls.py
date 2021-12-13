"""
Xperiencedezignwiz home app URL Configuration

URLs for the home app setup according to home/views.py
home = the homepage
the social media views are setup to authorise login via the
various social media apps.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rest-auth/facebook/',
         views.FacebookLogin.as_view(),
         name='fb_login'),
    path('rest-auth/twitter/',
         views.TwitterLogin.as_view(),
         name='twitter_login'),
    path('email/', views.send_email, name='send_email'),
    path('contact/', views. Contact.as_view(), name='contact'),

]
