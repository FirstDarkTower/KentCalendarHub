from django.conf.urls import patterns, url
from StudentSite import views

__author__ = 'Jarrek R. Holmes'

urlpatterns = patterns('',
                       url(r"^$",views.index, name = 'index'),
                       url(r"^teacher_list/$",views.teacher_list, name='teacher_list'),
                       url(r"^cal_id/$", views.get_cal_id, name='cal_key'),
                       url(r"^ms_page/$", views.ms_page, name='ms_page'),
                       url(r"^sixth_page/$", views.sixth_page, name="sixth_page"),
                       url(r"^sixth_rotations/$", views.sixth_rotations, name='sixth_rotations'),
                       url(r"^other_calendars/$", views.other_calendars, name='other_calendars')
)