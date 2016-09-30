#!/usr/bin/python

import shodan
import sys


SHODAN_API_KEY = "INSERT API KEY HERE"

api = shodan.Shodan(SHODAN_API_KEY)

i = 1
times = len(sys.argv)

while (i != times):
	
	try:

		try:
	        	results = api.host(sys.argv[i])
	

		        print 'Results found for: %s' % sys.argv[i]
		        for result in results['data']:
				print '======================================'
		                print 'IP: %s | PORT: %s' % (result['ip_str'], result['port'])
				print '======================================'
		                print result['data']
		                print ''
				i = i + 1
		except IndexError:
			print "Scanning finished."
			quit()

	except shodan.APIError, e:
	        print 'Error: %s' % e
