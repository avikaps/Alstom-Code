#!/usr/bin/env python

from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-x", "--xhtml",
                      action="store_true",
                      dest="xhtml_flag",
                      default=False,
                      help="create a XHTML template instead of HTML")
    parser.add_option("-c", "--cssfile",
                      action="store", # optional because action defaults to "store"
                      dest="cssfile",
                      default="style.css",
                      help="CSS file to link",)
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args
    class MyParser(OptionParser):
        def format_epilog(self, formatter):
            return self.epilog
    parser =MyParser(epilog=
"""Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -b BOARD TYPE, --board type=BOARD TYPE
                        Captures the SCU board type and creates an IP address
  -m START MEMORY, --start memory=START MEMORY
                        start address of the memory location in SCU
  -e END MEMORY, --end memory=END MEMORY
                        end address of the memory location in SCU
  -o ORIGIN PATH, --origin path=ORIGIN PATH
                        complete path where the file is currently located in
                        host computer
  -d DESTINATION PATH, --destination path=DESTINATION PATH
                        path where the file has to be place on to target board
  -r READ, --read=READ  read actioon will be perfromed on the SCU
  -w WRITE, --write=WRITE
                        write actin will be perfromed on the board
  -i INIT, --init=INIT  Innitalization will start up, SATA disk preperation
  -u UPLOAD, --upload=UPLOAD
                        start uploading the file to the installer embedded
  -t DOWNLOAD, --download=DOWNLOAD
                        download a file from the installer embedded
""")

if __name__ == '__main__':
    main()
