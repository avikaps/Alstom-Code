#!/usr/bin/python

import os
import csv
import collections
import sys

#Creating ordered dictionary for the predictor:

mapper_dict = collections.OrderedDict()
mapper_dict['id'] = 'Account ID', 'Lead ID', 'AccountID'
mapper_dict['email'] = 'Email', 'email', 'Email-Address', 'Email Address'
mapper_dict['First Name'] = 'First Name', 'FName', 'FirstName', 'FNAME', 'FIRST NAME'
mapper_dict['Last Name'] = 'Last Name', 'LName', 'LastName', 'LNAME', 'LAST NAME'
mapper_dict['Title'] = 'Title', 'JobTitle', 'Job Title'
mapper_dict['Company'] = 'Company Name', 'Account Name', 'Organization' , 'Company'
mapper_dict['Work Phone'] ='Phone', 'Work Phone', 'Business Phone', 'WorkPhone'
mapper_dict['Mobile Phone'] = 'Mobile', 'Mobile Phone', 'Personal Phone', 'MobilePhone'
mapper_dict['Address 1'] = 'Mailing Street 1', 'Mailing Street', 'Business Mailing Street', 'Address 1', 'Street 1', 'Street', 'Address'
mapper_dict['Address 2'] = 'Address 2', 'Street 2', 'Mailing Street 2'
mapper_dict['City'] = 'City', 'Mailing City'
mapper_dict['State'] = 'State', 'Mailing State/Province'
mapper_dict['Zip'] = 'Zip', 'Mailing Zip/Postal Code'actual_header = []
expected_header = []

#----------------------------------------------------------------------
#Function writes the list of headers
def header_processing(input_file, mapping_file):
    """
    This function create a mapping.txt file afterreading through the input file
    and creates a mapping file based on the predectied header names.
    """
    with open(INPUTFILE_PATH, 'rU') as input_file:
        read_input_file = csv.reader(input_file)
        input_headers = read_input_file.next()

    for actual_head, predicted_head in mapper_dict.iteritems():
        for each_column_header in input_header:
            #print each_column_header
            if (each_column_header in predicted_head):
                print "%s : %s" %(actual_head, each_column_header)
	print "%s :" %(actual_head)

    with open(mapping_file, 'wb') as map_file:
        for each_line in map_file:
            #print each_line
            expected_header.append(tuple(each_line.strip().split(":"))[0])
            actual_header.append(tuple(each_line.strip().split(":"))[1])
            #print actual_header
            #print expected_header

def write():
    print('Creating new text file') 

    name = input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'r+')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()


#----------------------------------------------------------------------
#Main function        
if __name__ == "__main__":
    start_time = time.time()
    try :
        INPUTFILE_PATH = sys.argv[1]
        OUTPUTFILE_PATH = sys.argv[2]
    except IndexError:
        print "\nUsage of the script is as shown below :"
        print "\n<script_name> <input_file_path> <output_directory>"
        print "\npython reoder_script.py ~/Downloads/tsm-leads-report-test.csv ~/Downloads/"
    if not os.path.exists(INPUTFILE_PATH):
        print os.path.basename(INPUTFILE_PATH), "- File not found !"
        sys.exit("File not found")
    if not os.path.exists(OUTPUTFILE_PATH):
        print os.path.dirname(OUTPUTFILE_PATH), "- Directory not found !"
        sys.exit("Directory not found")
    header_processing(INPUTFILE_PATH, OUTPUTFILE_PATH)

Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
>>> print "dict['Alice']: ", dict['Alice'];
dict['Alice']: 

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'
>>> print "dict['Name']: ", dict['Name'];
dict['Name']:  Zara
>>> print "dict['Age']: ", dict['Age'];
dict['Age']:  7
>>> dict = {'Name': ('Zara', 'Sara', 'Dara'), 'Age': (7,8,9), 'Class': ('First', 'Second', 'Third'};
	
SyntaxError: invalid syntax
>>> dict = {'Name': ('Zara', 'Sara', 'Dara'), 'Age': (7,8,9), 'Class': ('First', 'Second', 'Third')};
>>> print "dict['Age']: ", dict['Age'];
dict['Age']:  (7, 8, 9)
>>> dict.keys()
['Age', 'Name', 'Class']
>>> dict.values()
[(7, 8, 9), ('Zara', 'Sara', 'Dara'), ('First', 'Second', 'Third')]
>>> dict.get('Age')
(7, 8, 9)
>>> mapper_dict = {'id': ('Account ID', 'Lead ID', 'AccountID'),
               'email': ('Email', 'email', 'Email-Address', 'Email Address'),
               'First Name': ('First Name', 'FName', 'FirstName', 'FNAME', 'FIRST NAME'),
               'Last Name': ('Last Name', 'LName', 'LastName', 'LNAME', 'LAST NAME'),
               'Title': ('Title', 'JobTitle', 'Job Title'),
               'Company': ('Company Name', 'Account Name', 'Organization' , 'Company'),
               'Work Phone': ('Phone', 'Work Phone', 'Business Phone', 'WorkPhone'),
               'Mobile Phone': ('Mobile', 'Mobile Phone', 'Personal Phone', 'MobilePhone'),
               'Address 1': ('Mailing Street 1', 'Mailing Street', 'Business Mailing Street', 'Address 1', 'Street 1', 'Street', 'Address'),
               'Address 2': ('Address 2', 'Street 2', 'Mailing Street 2'),
               'City': ('City', 'Mailing City'),
               'State': ('State', 'Mailing State/Province'),
               'Zip': ('Zip', 'Mailing Zip/Postal Code')}
>>> mapper_dict.values()
[('City', 'Mailing City'), ('Zip', 'Mailing Zip/Postal Code'), ('Title', 'JobTitle', 'Job Title'), ('Phone', 'Work Phone', 'Business Phone', 'WorkPhone'), ('First Name', 'FName', 'FirstName', 'FNAME', 'FIRST NAME'), ('State', 'Mailing State/Province'), ('Mobile', 'Mobile Phone', 'Personal Phone', 'MobilePhone'), ('Account ID', 'Lead ID', 'AccountID'), ('Mailing Street 1', 'Mailing Street', 'Business Mailing Street', 'Address 1', 'Street 1', 'Street', 'Address'), ('Company Name', 'Account Name', 'Organization', 'Company'), ('Address 2', 'Street 2', 'Mailing Street 2'), ('Last Name', 'LName', 'LastName', 'LNAME', 'LAST NAME'), ('Email', 'email', 'Email-Address', 'Email Address')]
>>> mapper_dict.items()
[('City', ('City', 'Mailing City')), ('Zip', ('Zip', 'Mailing Zip/Postal Code')), ('Title', ('Title', 'JobTitle', 'Job Title')), ('Work Phone', ('Phone', 'Work Phone', 'Business Phone', 'WorkPhone')), ('First Name', ('First Name', 'FName', 'FirstName', 'FNAME', 'FIRST NAME')), ('State', ('State', 'Mailing State/Province')), ('Mobile Phone', ('Mobile', 'Mobile Phone', 'Personal Phone', 'MobilePhone')), ('id', ('Account ID', 'Lead ID', 'AccountID')), ('Address 1', ('Mailing Street 1', 'Mailing Street', 'Business Mailing Street', 'Address 1', 'Street 1', 'Street', 'Address')), ('Company', ('Company Name', 'Account Name', 'Organization', 'Company')), ('Address 2', ('Address 2', 'Street 2', 'Mailing Street 2')), ('Last Name', ('Last Name', 'LName', 'LastName', 'LNAME', 'LAST NAME')), ('email', ('Email', 'email', 'Email-Address', 'Email Address'))]
>>> 

>>> for actual_head, predicted_head in mapper_dict.iteritems():
	for each_column_header in input_header:
		#print each_column_header
		if (each_column_header in predicted_head):
			print "%s : %s" %(actual_head, each_column_header)
			x = ("%s : %s" %(actual_head, each_column_header))
			new_t.append(x)
	print "%s :" %(actual_head)
	y = ("%s :" %(actual_head))
	new_t.append(y)

>>> 
>>> for actual_head, predicted_head in mapper_dict.iteritems():
	for each_column_header in input_header:
		#print each_column_header
		if (each_column_header in predicted_head):
			print "%s : %s" %(actual_head, each_column_header)
			x = ("%s : %s" %(actual_head, each_column_header))
			new_t.append(x)
	print "%s :" %(actual_head)
	y = ("%s :" %(actual_head))
	new_t.append(y)

	
id : Lead ID
id :
email :
First Name : First Name
First Name :
Last Name : LastName
Last Name :
Title : JobTitle
Title :
Company :
Work Phone :
Mobile Phone :
Address 1 : Address
Address 1 :
Address 2 :
City : City
City :
State :
Zip :
>>> new_t
['id : Lead ID', 'id :', 'email :', 'First Name : First Name', 'First Name :', 'Last Name : LastName', 'Last Name :', 'Title : JobTitle', 'Title :', 'Company :', 'Work Phone :', 'Mobile Phone :', 'Address 1 : Address', 'Address 1 :', 'Address 2 :', 'City : City', 'City :', 'State :', 'Zip :']
>>> set(new_t)
set(['First Name : First Name', 'id : Lead ID', 'email :', 'Company :', 'Address 1 :', 'City :', 'id :', 'City : City', 'Zip :', 'Title :', 'Address 1 : Address', 'Work Phone :', 'State :', 'Address 2 :', 'Title : JobTitle', 'Last Name :', 'Last Name : LastName', 'Mobile Phone :', 'First Name :'])
>>> new_t
['id : Lead ID', 'id :', 'email :', 'First Name : First Name', 'First Name :', 'Last Name : LastName', 'Last Name :', 'Title : JobTitle', 'Title :', 'Company :', 'Work Phone :', 'Mobile Phone :', 'Address 1 : Address', 'Address 1 :', 'Address 2 :', 'City : City', 'City :', 'State :', 'Zip :']
>>> new_t[1]
'id :'
>>> new_t[0]
'id : Lead ID'
