from django.db import models

class Record(models.Model):	
   spot_id = models.IntegerField(unique=True)
   timestamp = models.DateTimeField()
   reporter = models.CharField(max_length=100)
   reporter_grid = models.CharField(max_length=6)
   snr = models.IntegerField()
   frequency = models.DecimalField(max_digits=10,decimal_places=5)
   call_sign = models.CharField(max_length=6)
   grid = models.CharField(max_length=6)
   power = models.IntegerField()
   drift = models.IntegerField()
   distance = models.IntegerField()
   azimuth = models.IntegerField()
   band = models.IntegerField()
   version = models.CharField(max_length=100,blank=True,null=True)
   code = models.PositiveIntegerField()

   def __unicode__(self):
      return unicode(self.spot_id)

