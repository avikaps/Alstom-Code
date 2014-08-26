#!/usr/bin/env python

import optparse
import MultipartPostHandler
import urllib2
import sys
import os


prog_name = "moon_installer.py"

# usefull when the program alters from the normal python file
prog_version = "%prog 0.1 Copyright (C) 2014 ALSTOM TRANSPORT"

prog_usage = "Usage: %prog [LOCATION] [PARAMETER(s)...] [SERVICE] "

prog_desc = "This code demonstrates the usage of Installer-CmdLine.\
 It will be provided with [LOCATION] [PARAMETER(s)...] and [SERVICES]\
 related to each option as guided in the detail usage to interact with the\
 Embedded Installer to display results to user."

mandatory_usage = '''
Please provide SCU Serial Number from 1 to 65535 and
SCU Board type either from 'A' / 'B' / 'G'

--serial XXXXX  --board-type A  are mandatory parameters

--help : to display a complete help menu. '''

read_usage = '''
Please use the Read FRAM service with the desired parameters

Usage : [LOCATION] [PARAMETER(s)...] [SERVICE]

--read-fuses     --serial XXXXX --board-type X --output <filepath> as parameter
--read-crc	 --serial XXXXX --board-type X --output <filepath> as parameter
--read-gid	 --serial XXXXX --board-type X --output <filepath> as parameter	
'''

write_usage = '''
Please use the Write FRAM service with the desired parameters

Usage : [LOCATION] [PARAMETER(s)...] [SERVICE]

--write-fuses    --serial XXXXX --board-type X --input <filepath> as parameter
--write-crc	 --serial XXXXX --board-type X --input <filepath> as parameter
--write-gid	 --serial XXXXX --board-type X --input <filepath> as parameter	
'''

def main():
    parser = optparse.OptionParser(usage=prog_usage, version=prog_version,
                                   description=prog_desc)
    location_opts = optparse.OptionGroup(parser, 'LOCATIONS', 'These are the'
                                       ' mandatory for all services.')
    location_opts.add_option("--board-type",help="\nString: SCU board channel"
                            " type. For Eg: 'A' or 'B' or 'G'",action="store",
                            type="string", dest="channel")
    location_opts.add_option("--serial", help="\nInt: SCU serial number"
                            " For Eg: 12345(numbers) ",action="store",
                            type="string", dest="serial")

    parser.add_option_group(location_opts)
    
    action_opts = optparse.OptionGroup(parser, 'SERVICES', 'These are the'
                                       ' services provided by offline-installer'
                                       '/cmdline-installer.')
    action_opts.add_option("--format-flash", help="\nThis service will FORMAT"
                           " the internal flash SATA memory. If a partition"
                           " is already defined for the electronic stamp,"
                           " then service will perform NO Action.",
                           action="callback",callback=formatflash)
    
    action_opts.add_option("--config-IP", help="\nThis service will calculate"
                           " the IP Address of the target SCU when serial"
                           "-number and the type of board is provided by user",
                           action="callback", callback=configIP)

    action_opts.add_option("--write-config", help="\nThis service enables user"
                           " to provide a configuration of one SCU board."
                           " Service then write config to flash memory.",
                           action="callback", callback=write_config)

    action_opts.add_option("--read-fuses", help="\n This service will read the"
                           " fields of Dyn_key data structure in FRAM based on"
                           " different channels.",action="callback",
                           callback=read_fuses)

    action_opts.add_option("--read-gid",  help="\nThis service will read a"
                           " string of hexadecimal format from FRAM data-"
                           "structure based on the channel type provided"
                           " by user",action="callback", callback=read_gid)

    action_opts.add_option("--read-crc",  help="\nThis service will read the"
                           " fields of data structure in FRAM based on"
                           " different channels.",action="callback",
                           callback=read_crc)

    action_opts.add_option("--write-fuses", help="\n This service will write"
                           " the Dyn_key data structure in FRAM based on the"
                           " channels and associated values provided by user",
                           action="callback", callback=write_fuses)

    action_opts.add_option("--write-crc", help="\nThis service will write a"
                           " string of hexadecimal format on to FRAM data-"
                           "structure based on the channel type provided"
                           " by user",action="callback", callback=write_crc)

    action_opts.add_option("--write-gid", help="\nThis service will write a"
                           " string of hexadecimal format on to FRAM data-"
                           "structure based on the channel type provided"
                           " by user",action="callback", callback=write_gid)

    action_opts.add_option("--download-from-SATA", help="\nThis service will"
                           " enable user to download the file from SATA Flash"
                           " based on the segment-ID, filepath and filename"
                           " inputs provided by user",action="callback",
                           callback=download)

    action_opts.add_option("--upload-to-SATA", help="\nThis service will enable"
                           " user to upload the file to SATA Flash memory based"
                           " on the segment-ID, filepath and filename inputs"
                           " provided by user",action="callback",
                           callback=upload)

    parser.add_option_group(action_opts)

    command_opts = optparse.OptionGroup(parser, 'Parameters','These are'
                                        ' parameters required to initiate'
                                        ' SERVICES provided by OFF-LINE '
                                        'Installer.')

    command_opts.add_option("--input", help="\nString: Depending on"
                            " the service, input is either a directory path"
                            " or a full file path. File path is either a"
                            " network file path (\\bipbipbip\MooN\Installer)"
                            " or a local file path(c:\data\MooN\Installer).",
                            action="store", type="string", dest="inputfilepath")
    command_opts.add_option("--output", help="\nString: Depending on the"
                            " service, output is either a directory path or a"
                            " full file path. File path is either a network"
                            " file path (\\bipbipbip\MooN\Installer) or a "
                            "local file path (C:\data\MooN\Installer).",
                            action="store", type="string", dest="outputfilepath")
    parser.add_option_group(command_opts)

    option, args = parser.parse_args()
    #print option
    #print args

    if option.serial == None or option.channel == None:
        print mandatory_usage, "\n\n", prog_usage
        # sys.exit(1)
        # parser.print_help()

def create_dir(filepath, filename):
        os.chdir(filepath)
        pwd = os.getcwd()
        file_path = pwd + "\\" + filename
        return file_path
    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        os.chdir(d)
    else :
        os.chdir(d)

def read_FRAM(hostIP, outputPath, memoryType, boardType, serial):
    print "Reading FRAM Values . . ."
    url = 'http://' + hostIP + '/cgi-bin/FRAM_Read.cgi'
    params = {'BoardType':boardType, 'MemoryType':memoryType }
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
    request = opener.open(url, params)
    file_content = request.read()

    filename = 'SCU_'+serial+'_Board_'+boardType+'_'+memoryType+'.bin'

    if outputPath.endswith(".bin"):
        write_file_content(outputPath, file_content)
    else:
        ensure_dir(outputPath)

        file_path = create_dir(outputPath, filename)
        write_file_content(file_path, file_content)

        
def write_file_content(filename, file_content):
    fh = open(filename, "wb")
    fh.write(file_content)
    fh.close()
    print "File has been succesfully downloaded to : ", filename


def write_FRAM(hostIP, inputPath, memoryType, boardType):
    print "Writing Values to FRAM . . ."
    url = 'http://' + hostIP + '/cgi-bin/FRAM_Write.cgi'
    if inputPath.endswith(".bin"):
        params = {'BoardType':boardType,
                  'WriteFile':file(inputPath, 'rb'),
                  'MemoryType':memoryType}
        opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)

        print opener.open(url, params).read()

def configIP(option, opt_str, value, parser):
    try :
        serial = int(parser.values.serial)
    except :
        print "Please provide an integer SCU Serial Number between 1 to 65535"
        sys.exit(1)
        
    print "Serial is : ", SERIAL
    channel = parser.values.channel
    print "Channel is : ",channel
    ip = compute_ip(serial, channel)
    print "Generated IP is ----> ", ip

def read_fuses(option, opt_str, value, parser):
    try :
        if not(parser.values.outputfilepath == None):
            outputPath = parser.values.outputfilepath
    except:
        print read_usage
        sys.exit(1)
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "reading Fuses Information . . ."

    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    
    memoryType = 'FUSE'
    boardType = parser.values.channel
    serial = parser.values.serial

    read_FRAM(hostIP, outputPath, memoryType, boardType, serial)
    
def read_crc(option, opt_str, value, parser):
    try :
        if not(parser.values.outputfilepath == None):
            outputPath = parser.values.outputfilepath
    except:
        print read_usage
        sys.exit(1)    
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "reading CRC Information . . ."
    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    memoryType = 'CRC'
    boardType = parser.values.channel
    serial = parser.values.serial

    read_FRAM(hostIP, outputPath, memoryType, boardType, serial)

def read_gid(option, opt_str, value, parser):
    try :
        if not(parser.values.outputfilepath == None):
            outputPath = parser.values.outputfilepath
    except:
        print read_usage
        sys.exit(1)
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "Read GID Information . . ."
    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    memoryType = 'GID'
    boardType = parser.values.channel
    serial = parser.values.serial

    read_FRAM(hostIP, outputPath, memoryType, boardType, serial)

def write_fuses(option, opt_str, value, parser):
    try :
        if not(parser.values.inputfilepath == None):
            inputPath = parser.values.inputfilepath
    except:
        print write_usage
        sys.exit(1)
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "Writing Fuses Information . . ."   

    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    
    memoryType = 'FUSE'
    boardType = parser.values.channel
    write_FRAM(hostIP, inputPath, memoryType, boardType)
   
 
def write_crc(option, opt_str, value, parser):
    try :
        if not(parser.values.inputfilepath == None):
            inputPath = parser.values.inputfilepath
    except:
        print write_usage
        sys.exit(1)
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "Writing CRC Information . . ."   

    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    
    memoryType = 'CRC'
    boardType = parser.values.channel
    write_FRAM(hostIP, inputPath, memoryType, boardType)
    
def write_gid(option, opt_str, value, parser):
    try :
        if not(parser.values.inputfilepath == None):
            inputPath = parser.values.inputfilepath
    except:
        print write_usage
        sys.exit(1)
    ip = compute_ip(parser.values.serial, parser.values.channel)
    print "Writing GID Information . . ."   

    print "Calculated host IP is : ", ip
    hostIP = '10.107.11.184'
    print "\nNot using the calculated IP but a default one :", hostIP
    
    memoryType = 'GID'
    boardType = parser.values.channel
    write_FRAM(hostIP, inputPath, memoryType, boardType)
    
def formatflash(option, opt_str, value, parser):
    print "Formatting Flash Memory . . ."    
def write_config(option, opt_str, value, parser):
    print "Writing Config file to flash . . ."    
def upload(option, opt_str, value, parser):
    print "Upload file to SATA . . ."    
def download(option, opt_str, value, parser):
    print "Download file from SATA . . ."

def compute_ip(serial, channel):
    try :
        serial = int(serial)
    except :
        print "Please provide an integer SCU Serial Number between 1 to 65535"
        sys.exit(1)
    serial, valid_serial = check_serial(serial)
    channel, valid_channel = check_channel(channel)
    if (valid_serial == 0) and (valid_channel == 0):
        msb = serial >> 8
        lsb = serial & 255
        ip_gateway = '10.'+ str(msb) + '.' + str(lsb) + '.1'
        ip_channel_a = '10.'+ str(msb) + '.' + str(lsb) + '.2'
        ip_channel_b = '10.'+ str(msb) + '.' + str(lsb) + '.3'
        if channel == 'A':
            # print "IP of Channel A is : ", ip_channel_a
            return ip_channel_a
        if channel == 'B':
            # print "IP of Channel B is : ", ip_channel_b
            return ip_channel_b
        else :
            # print "IP of Gateway is : ", ip_gateway
            return ip_gateway
    else :
        print "Serial number should be between 1 to 65535"
        print "and channel should be either from A/B/G"
        sys.exit(1)

def check_serial(serial):
    if ((serial == 0) or (serial > 65535)):
        print "Wrong SCU serial number - ", serial
        valid_serial = 1
        return serial, valid_serial
    else :
        valid_serial = 0
        return serial, valid_serial
        
    
def check_channel(channel):
    if ((channel == 'A') or (channel == 'B') or (channel == 'G')):
        valid_channel = 0
        return channel, valid_channel
    else:
        print "Incorrect Channel type - ", channel
        valid_channel = 1
        return channel, valid_channel


if __name__ == '__main__':
    main()
