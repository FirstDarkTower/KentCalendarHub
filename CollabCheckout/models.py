from django.db import models

# Create your models here.



class RoomSlots(models.Model):
    period = models.IntegerField()
    checkout_email = models.EmailField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    room = models.CharField(max_length=256)
    reserved = models.BooleanField()

    def __unicode__(self):
        return self.period + " "+ self.date + " " + self.room + " " +self.reserved
