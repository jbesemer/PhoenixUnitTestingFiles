#! env python

import os, os.path
import stat

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

	os.path.walk( path, Visit, args )

def Visit( args, dirname, files ):
	for filename in files:
		if( not filename.endswith( ".csv" )):
			continue

		print ":::",filename,":::"
		src = os.path.join( dirname, filename )
		count = 0
		for line in file( src ):
			print line,
			count += 1
			if count > 5:
				break
		print

if __name__ == "__main__":
	import sys

	# Main([ "PhoenixConnection", "PhoenixControlLibrary", "PhoenixLibrary" ])
	Main( sys.argv[ 1: ])
