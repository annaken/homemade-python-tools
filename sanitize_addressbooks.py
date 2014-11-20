import string
import random
import os
import re

outfile_invalid = open ("invalid",'w')

sourcedirname = "addressbooks-notnull"
destdirname = "addressbooks-strict"

emailpattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

for addressbook in os.listdir(sourcedirname):

	# Input file
	infile = open (sourcedirname + "/" + addressbook ,'r')
	outfile = open (destdirname + "/" + addressbook ,'w')

	# Read in file
	for line in infile.readlines():
		line = line.replace("\n","").split("|")

	# Format:
	# nickname|firstname|surname|email

		if re.match(emailpattern, line[3]):
			# valid
			outfile.write(line[0] + "|" + line[1] + "|" + line[2] + "|" + line [3] + "\n")

		else:
			# invalid
			outfile_invalid.write(addressbook + " : " + line[0] +  " : " + line[1] +  " : " + line[2] +  " : " + line[3] + "\n")


