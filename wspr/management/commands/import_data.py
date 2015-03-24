import csv
import datetime
import pytz

from django.core.management.base import BaseCommand, CommandError
from wspr.models import Record

class Command(BaseCommand):
	args = '<path to csv file> [optional filter]'
	help = 'Import the WSPR format data at the given path'
	ROW_LENGTH=15
	LOG_EVERY=1000

	def _import_row(self,row,filter):
		(spot_id, timestamp, reporter, reporter_grid, snr,freq,call_sign,grid,power,drift,
			distance,azimuth,band,version,code) = row
		if filter:
			if filter != reporter.lower() and filter != call_sign.lower():
				return
		try:
			record,created = Record.objects.get_or_create(spot_id=int(spot_id),
				defaults={'timestamp': datetime.datetime.utcfromtimestamp(int(timestamp)).replace(tzinfo=pytz.utc),
			'reporter': reporter,
			'reporter_grid': reporter_grid,
			'snr': int(snr),
			'frequency': freq,
			'call_sign': call_sign,
			'grid': grid,
			'power': int(power),
			'drift': int(drift),
			'distance': int(distance),
			'azimuth': int(azimuth),
			'band': int(band),
			'version': version,
			'code': int(code)})
			if created:
				print 'Added %s, %s->%s' % (spot_id, call_sign,reporter)
		except ValueError,e:
			print '   error loading row. %s' % e		

	def import_from_file(self,line_reader,filter,max_row=0):
		count=0
		for row in line_reader:
			count+=1
			if max_row and count > max_row:
				return
			if count % Command.LOG_EVERY == 0:
				print 'Processed %d' % count
			if len(row) != Command.ROW_LENGTH:
				print 'Row %d is wrong length. Expected %d, found %d' % (count,Command.ROW_LENGTH,len(row))
				return
			self._import_row(row,filter)

	def handle(self,*args,**kwargs):
		if len(args) < 1:
			return Command.help
		path = args[0]
		if len(args)> 1:
			filter = args[1]
		else:
			filter = None
		print 'Processing data at %s' % path
		if filter: 
			print 'with callsign filter %s' % filter
		print '---------------------'
		with open(path,'rU') as f:
			self.import_from_file(csv.reader(f),filter,max_row=0)

			
