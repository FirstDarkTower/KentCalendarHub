import os
from collections import OrderedDict
from datetime import date

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

def format_time(time):
    if len(time) > 3:
        mins = time[2:4]
        hours = time[:2]
    else:
        mins = time[1:3]
        hours = "0"+time[0:1]
    return hours +":"+mins

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCalendarHub.settings")
from StudentSite.models import Calendar
from CollabCheckout.models import RoomSlot
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

# print Calendar.objects.all()
#
# print Calendar.objects.filter(period = 6, school__in=[7,8])
#
# print_list(Calendar.objects.filter(school=6))
#
# print Calendar.objects.filter(school = 6, class_title__in=["6th Latin Language Arts", "6th Physical Education", "6th Writing Skills", "6th Arts Rotation", "6th Latin"], period=1)
#
# print Calendar.objects.filter(school="ELEC")
#
# class_name = "6th Science"
#
# print class_name.split("6th ")[1].lower()
#
# print Calendar.objects.filter(period=10, class_title="KDS Letter Days")


print_list(RoomSlot.objects.all())

periods=RoomSlot.objects.values_list('period').distinct()
new_periods = []
for period in periods:
    if period[0] == 0:
        temp = (0, "Before school")
    elif period[0] == 8:
        temp = (8, "After school: 3:30-4:30")
    elif period[0] == 9:
        temp = (9, "After school: 4:30-5:30")
    elif period[0] == 10:
        temp = (10, "First Half of Lunch")
    elif period[0] == 11:
        temp = (11, "Second Half og Lunch")
    else:
        temp = (period[0], period[0])
    new_periods.append(temp)

print new_periods

print_list(Calendar.objects.filter(period=1))

dateText = "8/20/2014"
period = 1

rooms = []
date_array = str(dateText).split("/")
d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
rooms = RoomSlot.objects.filter(period=period, date=d, reserved=False)

print rooms;