#! env python

import os, os.path
import re

MeterPattern = re.compile( "^Meter", re.IGNORECASE )
SensorPattern = re.compile( "^Sensor", re.IGNORECASE )
DatePattern = re.compile( "^Date", re.IGNORECASE )
TimestampPattern = re.compile( "^Timestamp", re.IGNORECASE )
MeasurementPattern = re.compile( "^Measurement", re.IGNORECASE )

StandardMeterPattern = re.compile( "^Meter S/N:", re.IGNORECASE )
StandardSensorPattern = re.compile( "^Sensor", re.IGNORECASE )

MaxLines = 20

class HeaderException( Exception ):
	def __init__( self, value ):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Header( object ):
	def __init__( self, filename ):
		self.RequiredLines = 3
		self.ExtraLines = 2
		self.HeaderIndex = -1
		self.DataIndex = -1
		self.HasTimestamps = False
		self.Lines = []

		self.fd = file( filename )

		self.Filename = filename
		self.Errors = ""
		self.Meter = MeterPattern.match( self.Readline())
		self.Sensor = SensorPattern.match( self.Readline())
		self.Date = DatePattern.match( self.Readline())
		self.Header = None

		if self.Meter:
			self.StandardMeter = StandardMeterPattern.match( self.Lines[ 0 ])
		else:
			self.Throw( "No Meter" )

		if self.Sensor:
			self.StandardSensor = StandardSensorPattern.match( self.Lines[ 1 ])
		else:
			self.Throw( "No Sensor" )

		# if not self.Date:
		#	self.Throw( "No Date" )

		self.FindHeader()
		self.GetData()

	def FindHeader( self ):
		for i in xrange( MaxLines - self.RequiredLines ):
			line = self.Readline()

			if TimestampPattern.match( line ):
				self.HasTimestamps = True
				self.Header = line
				self.HeaderIndex = len( self.Lines ) - 1
				return

			if MeasurementPattern.match( line ):
				self.HasTimestamps = False
				self.Header = line
				self.HeaderIndex = len( self.Lines ) - 1
				return
			# unrecognized header lines left in self.lines

		self.Throw( "No Headings" )

	def GetData( self ):
		self.Data = []
		for i in xrange( self.ExtraLines ):
			self.Data.append( self.Readline())

	def Readline( self ):
		line = self.fd.readline()
		if not line:
			return null
			self.Throw( "Premature EOF" )
		line = line.strip()
		self.Lines.append( line )
		return line

	def PresentAndStandard( self, present, standard ):
		if present and standard:
			return "S"
		else:
			return self.Present( present )

	def Present( self, present ):
		if present:
			return "Y"
		else:
			return "N"

	def Extra( self ):
		return len( self.Lines ) - self.ExtraLines - self.RequiredLines

	def __repr__( self ):
		return ",".join([
			self.PresentAndStandard( self.Header, self.HasTimestamps ),
			self.PresentAndStandard( self.Meter, self.StandardMeter ),
			self.PresentAndStandard( self.Sensor, self.StandardSensor ),
			self.Present( self.Date ),
			str( self.Extra()),
			self.Errors,
			self.Filename,
			])

	def Throw( self, message ):
		if self.Errors:
			self.Errors += "; "
		self.Errors += message
		if False:
			raise message

	Labels = ",".join([
			"Header",
			"Meter",
			"Sensor",
			"Date",
			"Extra",
			"Errors",
			"Filename",
			])


if __name__ == "__main__":
	import sys

	# Main([ "PhoenixConnection", "PhoenixControlLibrary", "PhoenixLibrary" ])
	# Main( sys.argv[ 1: ])
	print Header( sys.argv[1])
