import os


__author__ = 'Alex Clement'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCalendarHub.settings")
from StudentSite.models import Calendar
from StudentSite import views

temp = Calendar.objects.filter(period = 2, class_title__istartswith="AP")

temp = temp[0]

print temp.class_title

print views.get_teachers(temp.class_title, period = 2)

