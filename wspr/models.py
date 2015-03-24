from django.db import models
from django.db import connection

class RecordManager(models.Manager):
   def summarize_by_hour(self):
      cursor = connection.cursor()
      cursor.execute("""SELECT year,month,day,hour,count(*)
                        FROM wspr_record
                        GROUP BY year,month,day,hour""")
      results = []
      row = cursor.fetchone()
      while row:
         results.append(row)
         row = cursor.fetchone()
      
      return results

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

   # Denormalization to help with reporting
   year = models.IntegerField()
   month = models.IntegerField()
   day = models.IntegerField()
   hour = models.IntegerField()
   minutes = models.IntegerField()

   objects = RecordManager()

   def save(self,*args,**kwargs):
     self.year = self.timestamp.year
     self.month = self.timestamp.month
     self.day = self.timestamp.day
     self.hour = self.timestamp.hour
     self.minutes = self.timestamp.minute
     
     super(Record,self).save(*args,**kwargs)

   def __unicode__(self):
      return unicode(self.spot_id)

