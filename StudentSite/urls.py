from django.conf.urls import patterns, url
from StudentSite import views

__author__ = 'Jarrek R. Holmes'

urlpatterns = patterns('',
                       url(r"^$",views.index, name = 'index'),
)