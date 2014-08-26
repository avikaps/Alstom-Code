import StringIO
import os.path
import pycurl

def main():
    """
    http://curl.haxx.se/libcurl/c/curl_easy_setopt.html
    http://code.activestate.com/recipes/576422-python-http-post-binary-file-upload-with-pycurl/
    http://pycurl.cvs.sourceforge.net/pycurl/pycurl/tests/test_post2.py?view=markup
    """
    method = 4
    filename = './write_fram.bin'
    url = 'http://192.168.153.128/'

    c = pycurl.Curl()
    c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.URL, url)
    fout = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, fout.write)

    if method == 1:
        print "Method1"
        c.setopt(pycurl.HTTPPOST, [
                ("file1",
                 (c.FORM_FILE, filename))])
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/octet-stream'])
    elif method == 2:
        print "Method2"
        c.setopt(c.HTTPPOST, [
                ("uploadfieldname",
                 (c.FORM_FILE, filename,
                  c.FORM_CONTENTTYPE, "application/octet-stream"))])
    elif method == 3:
        print "Method3"
        c.setopt(pycurl.UPLOAD, 1)
        c.setopt(pycurl.READFUNCTION, open(filename, 'rb').read)
        filesize = os.path.getsize(filename)
        c.setopt(pycurl.INFILESIZE, filesize)
    elif method == 4:
        print "Method4"
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.HTTPHEADER, [
                'Content-Type: application/octet-stream'])

        filesize = os.path.getsize(filename)
        c.setopt(pycurl.POSTFIELDSIZE, filesize)
        fin = open(filename, 'rb')
        c.setopt(pycurl.READFUNCTION, fin.read)

    c.perform()
    response_code = c.getinfo(pycurl.RESPONSE_CODE)
    response_data = fout.getvalue()
    print response_code
    print response_data
    c.close()


if __name__ == '__main__':
    main()
