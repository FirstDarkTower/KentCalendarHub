__author__ = 'aclement'

import os

def format_time(time):
    if len(time) > 3:
        mins = time[2:4]
        hours = time[:2]
    else:
        mins = time[1:3]
        hours = "0"+time[0:1]
    return hours +":"+mins

def makeRoomSlot(period, start_time, end_time, date, room_number):
    date_array = date.split(" ")
    month = date_array[0]
    day = date_array[1]
    if month < 10:
        month = "0"+month
    if day < 10:
        day = "0"+month
    formated_date = date_array[2]+"-"+month+"-"+day
    r = RoomSlots.objects.get_or_create(period=period, start_time = format_time(start_time), end_time = format_time(end_time), date = formated_date, room = room_number, reserved=False)

    return r

def removeCalendar(cal_id):
    pass

def populate():
   from django.conf import settings
   fileName = os.path.join(os.path.join(settings.BASE_DIR, 'static'), 'Allperiods.csv')
   file = open(fileName)
   lines = file.readlines()[0].split('\r')
   for line in lines:
       lineArray = line.split(',')
       makeRoomSlot(lineArray[1], lineArray[2], lineArray[3], lineArray[0], lineArray[4])


if __name__ == "__main__":
    print "Populating Collab Slots.........."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCalendarHub.settings")
    from CollabCheckout.models import RoomSlots
    populate()
