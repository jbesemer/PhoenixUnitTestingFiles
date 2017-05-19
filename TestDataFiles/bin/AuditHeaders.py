#! env python

import os, os.path
import stat

import Header

Dot = "."
Verbose = 0

Errors = 0
Folders = []
Files = 0

def Main( args ):
	global Verbose
	path = Dot

	for arg in args:
		print arg
		if arg == "-v":
			Verbose = 1
		elif arg.startswith( "-" ):
			print "Unrecognized arg:", arg
		else:
			path = arg

	print Header.Header.Labels
	os.path.walk( path, Audit, args )

def Audit( args, dirname, files ):
	for filename in files:
		if( filename.endswith( ".csv" )):
			src = os.path.join( dirname, filename )
			try:
				print Header.Header( src )
			except:
				print "N,N,N,N,0,," + src

if __name__ == "__main__":
	import sys

	# Main([ "PhoenixConnection", "PhoenixControlLibrary", "PhoenixLibrary" ])
	Main( sys.argv[ 1: ])
