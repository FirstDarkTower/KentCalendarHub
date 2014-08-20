from django.conf.urls import patterns, url
from CollabCheckout import views

urlpatterns = patterns('',
                       url(r"^$",views.index, name = 'index'),
                       url(r"^period_list/$", views.period_list, name='period_list'),
                       )