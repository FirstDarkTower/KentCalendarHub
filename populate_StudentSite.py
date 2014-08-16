__author__ = 'Jarrek R. Holmes'
import os


def makeCalendar(period, class_title, teacher_name, cal_id, school):
    c = Calendar.objects.get_or_create(period = period, class_title = class_title, teacher_name = teacher_name, cal_id = cal_id, school=school)
    return c

def removeCalendar(cal_id):
    pass

def populate():
   from django.conf import settings
   fileName = os.path.join(os.path.join(settings.BASE_DIR, 'static'), 'CompletedCourses.tsv')
   file = open(fileName)
   file.readlines(1)
   for line in file:
        lineArray = line.split('\t')
        makeCalendar(lineArray[0], lineArray[2], lineArray[3].strip('"'), lineArray[7], lineArray[1])

if __name__ == "__main__":
    print "Populating Student Site.........."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCalendarHub.settings")
    from StudentSite.models import Calendar
    populate()