import requests
from lxml import html
import time
import re
import os
import sys

def ValConvert(val):
  if type(val).__name__ == 'unicode':
    return val.encode('utf8')
  elif type(val).__name__ == 'str':
    return val
  else:
    return str(val)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# List for storing previous pastes. We use this to check previous ones.
previousPastes = list()


# Setting parameters
checkUrls = None
moreUrls  = None
regexFile = None

try:
	checkUrls = float(sys.argv[1])
except:
	if checkUrls is None:
		checkUrls = float(0.5)
try:
	moreUrls = float(sys.argv[2])
except:
	if moreUrls is None:
		moreUrls  = float(15.5)

try:
	regexFile = sys.argv[3]
except:
	if regexFile is None:
		regexFile = 'regex.txt'


# My mega loop.
while True:

	# Getting the URL from the archive. We must be locked out.
	getPasteURL = requests.get('http://pastebin.com/archive')
	content = html.fromstring(getPasteURL.content)

	# Get all links and only take the 8 which list the most recent pasties.
	urlsa = content.xpath('//@href')
	urls = urlsa[13:21]


	# Start checking all of the extracted URLs.
	for item in urls:


		# If it has been checked previously, do nothing.
		if item in previousPastes:

			pass

		else:

			# IMPORTANT = add current item in the previousPastes array.
			previousPastes.append(item)

			# Getting raw paste data.
			print 'Checking http://pastebin.com/raw' + item
			temporario = requests.get('http://pastebin.com/raw' + item)

			with open('regex.txt') as file:

				regex = file.readlines()

				for line in regex:

					# Cleaning the regex and inserting into array.
					cleanwhitespace = "".join(line.split())
					storeInList = cleanwhitespace.split(",")

					regex      	  =	storeInList[0]
					outputFile 	  = storeInList[1]
					directoryName = storeInList[2]
					
					#Compiling regex to prepare for matching.
					compileRegex = re.compile(regex, re.IGNORECASE)

					#print re.match(compileRegex, temporario.text)

					if re.match(compileRegex, temporario.text) != None:
						
						output = open(outputFile, 'a+')
						output.write('=' * 30)
						output.write("\nFound something on: http://pastebin.com/raw" + item + "\n\n")
						output.write(ValConvert(temporario.text))
						print(temporario.text)
						print bcolors.OKGREEN + "Found something on: http://pastebin.com/raw" + item + bcolors.ENDC

			# Sleeper to accomodate for low network speeds.
			time.sleep(checkUrls)
			
	time.sleep(moreUrls)
