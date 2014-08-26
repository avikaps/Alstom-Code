import httplib, os, urllib2
import MultipartPostHandler

url = 'http://10.107.11.184/cgi-bin/FRAM_Read.cgi'
path = 'C:\\Avi Kapoor\\Moon_Installer\\Py_Interface\\fram_new.bin'
params = {'BoardType':'A', 'MemoryType':'ASASA' }
opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
request = opener.open(url, params)

print request.read()
filename = 'read_fram.bin'

def create_filename(filename):
    pwd = os.getcwd()
    file_path = pwd + "\download\\" + filename
    ensure_dir(file_path)
    return file_path
    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        os.chdir(d)
    else :
        os.chdir(d)

#ensure_dir(filename)
file_path = create_filename(filename)

fh = open(filename, "wb")

# read from request while writing to file
fh.write(request.read())

fh.close()

'''
import urllib2
import os

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

ip = "10.107.11.184"
cgi_action = './cgi-bin/FRAM_Read.cgi?ReadFram=A&checklist=CRC'
filename = "fram_read.bin"

def create_filename(filename):
    pwd = os.getcwd()
    file_path = pwd + "\download\\" + filename
    print file_path
    ensure_dir(file_path)
    return file_path
    
def ensure_dir(f):
    print f
    d = os.path.dirname(f)
    print d
    if not os.path.exists(d):
        os.makedirs(d)
        os.chdir(d)
    else :
        os.chdir(d)

httpService = httplib.HTTPConnection(ip)
httpService.request("GET", cgi_action)

response = httpService.getresponse()

if response.status == httplib.OK:
   print "Output from CGI request"
   # printText (response.read())
   # if response.read() == None
    

#copy response to variable because reading clears it

url = "http://" + ip + "/download/" + filename

print "url is : ", url

req = urllib2.urlopen(url)

#ensure_dir(filename)
file_path = create_filename(filename)

print "File path is :", file_path

print os.getcwd()

fh = open(filename, "wb")

# read from request while writing to file
fh.write(req.read())

fh.close()

# print "\n Data is ------------->\n", data 
#t = MyParse()
#t.feed(data)     #where the action happens
'''
