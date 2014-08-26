import MultipartPostHandler
import urllib2

url = 'http://10.107.11.184/cgi-bin/FRAM_Write.cgi'
path = "C:\Avi Kapoor\Moon_Installer\Py_Interface\crc_new_fram.bin"
params = {'BoardType':'A', 'WriteFile' : file(path, 'rb'), 'MemoryType':'CRC' }
opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
print opener.open(url, params).read()

'''
[def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

ip = "10.107.11.184"
cgi_action = './cgi-bin/FRAM_Write.cgi'
filename = 'write_fram.bin'

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
httpService.request("POST", cgi_action)

response = httpService.getresponse()

if response.status == httplib.OK:
   print "Output from CGI request"
   # printText (response.read())
   # if response.read() == None
    

#copy response to variable because reading clears it
'''

