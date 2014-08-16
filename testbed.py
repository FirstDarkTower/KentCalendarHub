import os
from collections import OrderedDict

__author__ = 'Alex Clement'


def remove_duplicates(list):
    new_list = []
    seen = set()
    for e in list:
        value = e.class_title
        if value not in seen:
            new_list.append(e)
            seen.add(value)

    return new_list

def print_list(list):
    for e in list:
        print e


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCalendarHub.settings")
from StudentSite.models import Calendar
from StudentSite import views

# temp = Calendar.objects.filter(period = 2, class_title__istartswith="AP")
#
# temp = temp[0]
#
# print temp.class_title
#
# print views.get_teachers(temp.class_title, period = 2)
#
# temp_list = Calendar.objects.filter(period=1)
#
# print_list(temp_list)
#
# print '__________________________________________'
# print_list(remove_duplicates(temp_list))

print Calendar.objects.filter(period = 6, school__in=[7,8])

print_list(Calendar.objects.filter(school=6))

print Calendar.objects.filter(school = 6, class_title__in=["6th Latin Language Arts", "6th Physical Education", "6th Writing Skills", "6th Arts Rotation", "6th Latin"], period=1)

print Calendar.objects.filter(school="ELEC")
