#!/usr/bin/env python

import subprocess
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '.'))

for test_case, test_number in zip(open('.\TEST_CASES.txt'), range(500)):
	# print test_number, test_case
	test_number = int(test_number) + 1
	sys.stdout.flush()
	proc = subprocess.Popen(test_case, stdout=subprocess.PIPE, shell=True)
	# print proc
	print '======================================================================'
	print '\nTEST CASE : ' + str(test_number)
	print '\nCOMMAND ' + str(test_number) + ' : ' + test_case
	(out, err) = proc.communicate()
	print '\nTEST OUTPUT:', out
	print '\nTEST ERROR:', err
	print '======================================================================'

