#!/usr/bin/env python

""" Moon Installer command line interface module moon_installer.py
@copyright: All rights reserved. (c) 2014. ALSTOM TRANSPORT.
This computer program may not be used, copied, distributed, corrected,
modified, translated, transmitted or assigned without ALSTOM's prior
written authorization. """

import os
import sys
import imp
import urllib2
import optparse
import MultipartPostHandler


# Print variables are used to capture all the default statements
VERSION = "%prog 0.4 Copyright (C) 2014 ALSTOM TRANSPORT"

USAGE = "Usage: %prog [LOCATION] [PARAMETER(s)...] [SERVICE] "

DESCRIPTION = "This code demonstrates the usage of Installer-CmdLine.\
 It will be provided with [LOCATION] [PARAMETER(s)...] and [SERVICES]\
 related to each option as guided in the detail usage to interact with the\
 Embedded Installer to display results to user."

# Print usage when any of the mandatory parameters are missing
MANDATORY_USAGE = '''
Please provide SCU Serial Number from 1 to 65535 and SCU Board type either
from 'A' / 'B' / 'G'

--serial xxxxx --board-type x are mandatory parameters

--help : to display a complete help menu.'''

# Print usage when encounter with any error in READ functionality
READ_USAGE = '''
Please use the Read FRAM service with the desired parameters

Usage : [LOCATION] [PARAMETER(s)...] [SERVICE]

--serial xxxxx --board-type x --output <filepath> as parameter    --read-fuses
--serial xxxxx --board-type x --output <filepath> as parameter    --read-crc
--serial xxxxx --board-type x --output <filepath> as parameter    --read-gid'''

# Print usage when encounter with any error in WRITE functionality
WRITE_USAGE = '''
Please use the Write FRAM service with the desired parameters

Usage : [LOCATION] [PARAMETER(s)...] [SERVICE]

--serial xxxxx --board-type x --input <filepath> as parameter    --write-fuses
--serial xxxxx --board-type x --input <filepath> as parameter    --write-crc
--serial xxxxx --board-type x --input <filepath> as parameter    --write-gid'''


# Defination of the ERROR CODES
ERROR_200 = "\n[ERROR:200] - MANDATORY PARAMTERS ARE MISSING"
ERROR_201 = "\n[ERROR:201] - INVALID SCU SERIAL NUMBER"
ERROR_202 = "\n[ERROR:202] - SCU SERIAL NUMBER OUT OF BOUNDS"
ERROR_203 = "\n[ERROR:203] - INVALID CHANNEL TYPE"
ERROR_204 = "\n[ERROR:204] - P_MOON_PRIVATE_IP_BASE.txt FILE NOT FOUND"
ERROR_205 = "\n[ERROR:205] - IP IS NOT GENERATED"
ERROR_206 = "\n[ERROR:206] - INVALID INPUT - IP COMPUTATION FAILED AND EXIT"
ERROR_207 = "\n[ERROR:207] - IP COMPUTATION FAILED AND EXIT!!"
ERROR_208 = "\n[ERROR:208] - MISSING BINARY FILE FOR THIS SERVICE"
ERROR_209 = "\n[ERROR:209] - PARAMETER NOT ASSOCIATED WITH THIS SERVICE"
ERROR_210 = "\n[ERROR:210] - INCORRECT SERVICE OPTION PROVIDED"
ERROR_211 = "\n[ERROR:211] - FILE PROVIDED CANNOT BE OPENED"
ERROR_212 = "\n[ERROR:212] - WRITE CONFIG REQUIRES 'tar.gz' FILE"
ERROR_213 = "\n[ERROR:213] - OUTPUT IS MISSING"
ERROR_214 = "\n[ERROR:214] - INPUT IS MISSING"


#HTTP ERROR HANDLING CODES
ERROR_300 = "\n[ERROR:300] - CONNECTION WAS ATTEMPTED TO UNREACHABLE NETWORK"
ERROR_301 = "\n[ERROR:301] - FAILED TO RECEIVE WEB-SERVER RESPONSE AND EXIT"


# Main function for Option paring
def main():
    """Main function of the program where all the parameters provided by the
    are parsed and options, arguments are stored in their respective variables.
    This has been classified in THREE different groups viz a viz
    as LOCATIONS PARAMETERS and SERVICES."""
    parser = optparse.OptionParser(usage=USAGE, version=VERSION,
                                   description=DESCRIPTION)
    location_opts = optparse.OptionGroup(parser, 'LOCATIONS', 'These are the'
                                         ' mandatory for all services.')
    location_opts.add_option("--board-type", help="\nString: SCU board channel"
                             " type. For Eg: 'A' or 'B' or 'G'",
                             action="store", type="string", dest="channel")
    location_opts.add_option("--serial", help="\nInt: SCU serial number"
                             " For Eg: 12345(numbers) ", action="store",
                             type="string", dest="serial")
    parser.add_option_group(location_opts)
    command_opts = optparse.OptionGroup(parser, 'Parameters', 'These are'
                                        ' parameters required to initiate'
                                        ' SERVICES provided by OFF-LINE '
                                        'Installer.')
    command_opts.add_option("--input", help="\nString: Depending on"
                            " the service, input is either a directory path"
                            " or a full file path. File path is either a"
                            " network file path (\\bipbipbip\MooN\Installer)"
                            " or a local file path(c:\data\MooN\Installer).",
                            action="store", type="string",
                            dest="inputfilepath")
    command_opts.add_option("--output", help="\nString: Depending on the"
                            " service, output is either a directory path or a"
                            " full file path. File path is either a network"
                            " file path (\\bipbipbip\MooN\Installer) or a "
                            "local file path (C:\data\MooN\Installer).",
                            action="store", type="string",
                            dest="outputfilepath")
    parser.add_option_group(command_opts)
    action_opts = optparse.OptionGroup(parser, 'SERVICES', 'These are the '
                                       'services provided by offline-installer'
                                       '/cmdline-installer.')
    action_opts.add_option("--format-flash", help="\nThis service will FORMAT"
                           " the internal flash SATA memory. If a partition"
                           " is already defined for the electronic stamp,"
                           " then service will perform NO Action.",
                           action="callback", callback=format_flash)
    action_opts.add_option("--config-ip", help="\nThis service will calculate"
                           " the IP Address of the target SCU when serial"
                           "-number and the type of board is provided by user",
                           action="callback", callback=config_ip)
    action_opts.add_option("--write-config", help="\nThis service enables user"
                           " to provide a configuration of one SCU board."
                           " Service then write config to flash memory.",
                           action="callback", callback=write_config)
    action_opts.add_option("--read-fuses", help="\n This service will read the"
                           " fields of Dyn_key data structure in FRAM based on"
                           " different channels.", action="callback",
                           callback=read_fuses)
    action_opts.add_option("--read-gid",  help="\nThis service will read a"
                           " string of hexadecimal format from FRAM data-"
                           "structure based on the channel type provided"
                           " by user", action="callback", callback=read_gid)
    action_opts.add_option("--read-crc", help="\nThis service will read the"
                           " fields of data structure in FRAM based on"
                           " different channels.", action="callback",
                           callback=read_crc)
    action_opts.add_option("--write-fuses", help="\n This service will write"
                           " the Dyn_key data structure in FRAM based on the"
                           " channels and associated values provided by user",
                           action="callback", callback=write_fuses)
    action_opts.add_option("--write-crc", help="\nThis service will write a"
                           " string of hexadecimal format on to FRAM data-"
                           "structure based on the channel type provided"
                           " by user", action="callback", callback=write_crc)
    action_opts.add_option("--write-gid", help="\nThis service will write a"
                           " string of hexadecimal format on to FRAM data-"
                           "structure based on the channel type provided"
                           " by user", action="callback", callback=write_gid)
    action_opts.add_option("--download-from-SATA", help="\nThis service will"
                           " enable user to download the file from SATA Flash"
                           " based on the segment-ID, file-path and file-name"
                           " inputs provided by user", action="callback",
                           callback=download)
    action_opts.add_option("--upload-to-SATA", help="\nThis Service will "
                           "enable user to upload the file to SATA Flash "
                           "memory based on the segment-ID, file-path and "
                           "file-name inputs provided by user",
                           action="callback", callback=upload)
    parser.add_option_group(action_opts)
    option, args = parser.parse_args()  # pylint'args'error has to b suppressed
    if not((option.serial is None) or (option.channel is None)):
        check_serial(option.serial)
        check_channel(option.channel)
    else:
        parser.print_help()
        print MANDATORY_USAGE
        sys.exit(ERROR_200)


def write_parameter_check(inputfile, outputfile):
    """write_parameter_check this checks the parameters required by
    write services"""
    try:
        if inputfile is None:
            print WRITE_USAGE
            sys.exit(ERROR_214)
        elif not (outputfile is None):
            sys.exit(ERROR_209)
        elif not inputfile.endswith('.bin'):
            sys.exit(ERROR_208)
        else:
            file(inputfile, 'rb')
    except IOError:
        sys.exit(ERROR_211)


def read_parameter_check(inputfile, outputfile):
    """read_parameter_check - this checks the parameters required by
    read services"""
    try:
        if outputfile is None:
            print READ_USAGE
            sys.exit(ERROR_213)
        elif not (inputfile is None):
            sys.exit(ERROR_209)
        else:
            print "\nAll checks passed"
    except Exception, raised_exception:
        print "\nException is :", raised_exception


def check_paramters_required(opt_str, inputfile, outputfile):
    """check_paramters_required checks what all parameters are required
    by each service for its uninteruppted execution."""
    if opt_str == '--write-config':
        try:
            if inputfile is None:
                sys.exit(ERROR_209)
            elif not (outputfile is None):
                sys.exit(ERROR_209)
            elif not inputfile.endswith('.tar.gz'):
                sys.exit(ERROR_212)
            else:
                file(inputfile, 'rb')
        except IOError:
            sys.exit(ERROR_211)
    elif opt_str == '--write-fuses':
        write_parameter_check(inputfile, outputfile)

    elif opt_str == '--write-gid':
        write_parameter_check(inputfile, outputfile)

    elif opt_str == '--write-crc':
        write_parameter_check(inputfile, outputfile)

    if opt_str == '--read-fuses':
        read_parameter_check(inputfile, outputfile)

    if opt_str == '--read-crc':
        read_parameter_check(inputfile, outputfile)

    if opt_str == '--read-gid':
        read_parameter_check(inputfile, outputfile)

    # if opt_str == '--download-from-SATA'
    # if opt_str == '--upload-to-SATA'--read-fuses


def create_dir(dirpath, filename):
    """Appends the file-name in the file-path provided by user"""
    os.chdir(dirpath)
    pwd = os.getcwd()
    file_path = pwd + "\\" + filename
    return file_path


def ensure_dir(outputpath):
    """Function ensures that the directory structure provided by user
    is correct"""
    dir_path = os.path.dirname(outputpath)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        os.chdir(dir_path)
    else:
        os.chdir(dir_path)


def read_fram(host_ip, output_path, memory_type, board_type, serial):
    """Generic FRAM read function used by read_crc, read_fuse and read_gid
    modules. This function reads the FRAM content by creating and sending a
    HTTP request to the HostIP of the SCU. read_fram internally calls
    write_file_content module to write the received content in a file."""
    print "\nReading FRAM Values . . ."
    url = 'http://' + host_ip + '/cgi-bin/FRAM_Read.cgi'
    params = {'BoardType': board_type, 'MemoryType': memory_type}
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
    try:
        response = opener.open(url, params)
    except urllib2.URLError:
        sys.exit(ERROR_300)
    valid_response = check_response_received(response)
    if not(valid_response is 0):
        sys.exit(ERROR_301)
    else:
        file_content = response.read()
    filename = 'SCU_'+serial+'_Board_'+board_type+'_'+memory_type+'.bin'
    if output_path.endswith(".bin"):
        print "\nWARNING - File will be overwritten with new response received"
        write_file_content(output_path, file_content)
    else:
        ensure_dir(output_path)
        file_path = create_dir(output_path, filename)
        write_file_content(file_path, file_content)


def write_file_content(file_path, file_content):
    """Writes the content to the file - called by read_fram module but
    indirectly used by read_crc, read_fuses and read_gid modules."""
    file_handler = open(file_path, "wb")
    file_handler.write(file_content)
    file_handler.close()
    print "\nFile has been successfully downloaded to : ", file_path


def write_fram(host_ip, input_path, memory_type, board_type):
    """Generic FRAM write function used by write_crc, write_fuse and write_gid
    modules. This function writes the FRAM content provided by user in a
    binary file over a HTTP request to the HostIP of SCU."""
    print "\nWriting Values to FRAM . . ."
    url = 'http://' + host_ip + '/cgi-bin/FRAM_Write.cgi'
    if input_path.endswith(".bin"):
        params = {'BoardType': board_type,
                  'WriteFile': file(input_path, 'rb'),
                  'MemoryType': memory_type}
        opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
        try:
            response = opener.open(url, params)
        except urllib2.URLError:
            sys.exit(ERROR_300)
        valid_response = check_response_received(response)
        if not(valid_response is 0):
            sys.exit(ERROR_301)
        else:
            print response.read()
    else:
        sys.exit(ERROR_208)


def config_ip(option, opt_str, value, parser):
    """Calculate the IP address of the SCU, based on the serial number and
    channel type of the target machine provided by the user."""
    try:
        serial = int(parser.values.serial)
    except ValueError:
        sys.exit(ERROR_201)
    channel = parser.values.channel
    host_ip = compute_ip(serial, channel)
    if not(host_ip is None):
        print "\nSerial is : ", serial
        print "\nChannel is : ", channel
        print "\nComputed IP is : ", host_ip
    else:
        sys.exit(ERROR_207)


def format_flash(option, opt_str, value, parser):
    """format_flash put a request to the webserver to check the partition
    created on the SATA are correct or NOT. It also checks whether it requires
    INIT or REINIT functionality."""
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nChecking Flash Memory . . ."
    print "\nComputed host IP is : ", host_ip
    url = 'http://' + host_ip + '/cgi-bin/SATA_Format.cgi'
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        sys.exit(ERROR_300)
    valid_response = check_response_received(response)
    if not(valid_response is 0):
        sys.exit(ERROR_301)
    else:
        print response.read()


def check_response_received(response):
    """check_request_received check the status and the code of the request
    received after sending a request to a WEB-SERVER"""
    try:
        if not (response.code is 200) and (response.msg is 'OK'):
            print "\nRequest not received from Web-Server"
            valid_response = 1
            return valid_response
        else:
            valid_response = 0
            return valid_response
    except urllib2.HTTPError:
        valid_response = 1
        return valid_response
    except Exception:
        print "\nGeneric Exception Raised"
        valid_response = 1
        return valid_response


def write_config(option, opt_str, value, parser):
    """write_config checks the partition in the SATA and writes the
    configuration files in SATA. This function requires Input config file
    as a paramter and the same will get uploaded to the SCU by Web-Server"""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nWriting Configuration file to Flash . . ."
    print "\nComputed Host-IP is : ", host_ip
    url = 'http://' + host_ip + '/cgi-bin/SATA_Config.cgi'
    input_path = parser.values.inputfilepath
    board_type = parser.values.channel
    params = {'BoardType': board_type,
              'SataConfigFile': file(input_path, 'rb')}
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
    try:
        response = opener.open(url, params)
    except urllib2.URLError:
        sys.exit(ERROR_300)
    valid_response = check_response_received(response)
    if not(valid_response is 0):
        sys.exit(ERROR_301)
    else:
        print response.read()


def read_fuses(option, opt_str, value, parser):
    """read_fuses will read FUSES information from FRAM, based on the channel
    type and internally calls read_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    output_path = parser.values.outputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nReading FUSES Information . . ."
    print "\nComputed host IP is : ", host_ip
    memory_type = 'FUSE'
    board_type = parser.values.channel
    serial = parser.values.serial
    read_fram(host_ip, output_path, memory_type, board_type, serial)


def read_crc(option, opt_str, value, parser):
    """read_crc will read CRC information from FRAM, based on the channel
    type and internally calls read_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    output_path = parser.values.outputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nReading CRC Information . . ."
    print "\nComputed host IP is : ", host_ip
    memory_type = 'CRC'
    board_type = parser.values.channel
    serial = parser.values.serial
    read_fram(host_ip, output_path, memory_type, board_type, serial)


def read_gid(option, opt_str, value, parser):
    """read_gid will read GID information from FRAM, based on the channel
    type and internally calls read_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    output_path = parser.values.outputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nReading GID Information . . ."
    print "\nComputed host IP is : ", host_ip
    memory_type = 'GID'
    board_type = parser.values.channel
    serial = parser.values.serial
    read_fram(host_ip, output_path, memory_type, board_type, serial)


def write_fuses(option, opt_str, value, parser):
    """write_fuses will create a request to write, the FUSE information
    provided by the user into FRAM, based on the channel type.
    This function internally calls write_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    input_path = parser.values.inputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nWriting FUSES Information . . ."
    print "\nComputed host IP is : ", host_ip
    memory_type = 'FUSE'
    board_type = parser.values.channel
    write_fram(host_ip, input_path, memory_type, board_type)


def write_crc(option, opt_str, value, parser):
    """write_crc will create a request to write, the CRC information
    provided by the user into FRAM, based on the channel type.
    This function internally calls write_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    input_path = parser.values.inputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nWriting CRC Information . . ."
    print "\nComputed host IP is : ", host_ip
    memory_type = 'CRC'
    board_type = parser.values.channel
    write_fram(host_ip, input_path, memory_type, board_type)


def write_gid(option, opt_str, value, parser):
    """write_gid will create a request to write, the GID information
    provided by the user into FRAM, based on the channel type.
    This function internally calls write_fram module to send HTTP request."""
    check_paramters_required(opt_str,
                             parser.values.inputfilepath,
                             parser.values.outputfilepath)
    input_path = parser.values.inputfilepath
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nWriting GID Information . . ."
    print "\Computed host IP is : ", host_ip
    memory_type = 'GID'
    board_type = parser.values.channel
    write_fram(host_ip, input_path, memory_type, board_type)


def upload(option, opt_str, value, parser):
    """upload description"""
    print "\nUpload file to SATA . . ."
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nComputed host IP is : ", host_ip
    # host_ip = '10.107.11.184'  # Subjected to change ip -->> host_ip
    # print "\nNot using the calculated IP but a default one :", host_ip
    url = 'http://' + host_ip + '/cgi-bin/SATA_Upload.cgi'
    input_path = parser.values.inputfilepath
    output_path = parser.values.outputfilepath
    board_type = parser.values.channel
    params = {'BoardType': board_type,
              'DestPath': output_path,
              'SataFile': file(input_path, 'rb')}
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
    try:
        response = opener.open(url, params)
    except urllib2.URLError:
        print ERROR_300
    valid_response = check_response_received(response)
    if not(valid_response is 0):
        sys.exit(ERROR_301)
    else:
        print response.read()


def download(option, opt_str, value, parser):
    """download description"""
    print "\nDownload file from SATA . . ."
    host_ip = compute_ip(parser.values.serial, parser.values.channel)
    print "\nComputed host IP is : ", host_ip
    url = 'http://' + host_ip + '/cgi-bin/SATA_Upload.cgi'
    input_path = parser.values.inputfilepath
    output_path = parser.values.outputfilepath
    board_type = parser.values.channel
    params = {'BoardType': board_type,
              'DownFrom': input_path,
              'UploadTo': output_path}
    opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
    try:
        response = opener.open(url, params)
    except urllib2.URLError:
        print ERROR_300
    valid_response = check_response_received(response)
    if not(valid_response is 0):
        sys.exit(ERROR_301)
    else:
        file_content = response.read()
        ensure_dir(output_path)
        file_path = create_dir(output_path, filename)
        write_file_content(file_path, file_content)


def compute_ip(serial, channel):
    """compute_ip is a generic function used by all the SERVICES to compute
    the host_ip for the SCU based on the serial number and the channel type
    provided by the user"""
    serial, valid_serial = check_serial(serial)
    channel, valid_channel = check_channel(channel)
    if (valid_serial == 0) and (valid_channel == 0):
        bin_val = bin(int(str(hex(serial)), 16))[2:]
        if not len(bin_val) == 16:
            first_two_bytes = (16 - len(bin_val))*'0' + bin_val
        else:
            first_two_bytes = bin_val
        byte_3 = str(int(first_two_bytes[0:8], 2))
        byte_4 = str(int(first_two_bytes[8:], 2))
        base_ip = read_moon_base_ip()
        byte_1 = ((base_ip.split('.', 1))[0])
        if channel == 'A':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 2)
            ip_channel_a = byte_1 + '.' + byte_2 + '.' + byte_3 + '.' + byte_4
            return ip_channel_a
        if channel == 'B':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 3)
            ip_channel_b = byte_1 + '.' + byte_2 + '.' + byte_3 + '.' + byte_4
            return ip_channel_b
        if channel == 'G':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 1)
            ip_gateway = byte_1 + '.' + byte_2 + '.' + byte_3 + '.' + byte_4
            return ip_gateway
        else:
            print ERROR_205  # Coverage can't be achieved. Defensive Code. 
            return None
    else:
        sys.exit(ERROR_206)


def read_moon_base_ip():
    """read_moon_base_ip reads the P_MOON_PRIVATE_IP_BASE value written in the
    P_MOON_PRIVATE_IP_BASE.txt file and returns the value to the caller"""
    try:
        file_handler = (open('.\P_MOON_PRIVATE_IP_BASE.txt'))
        data = imp.load_source('data', '', file_handler)
        base_ip = data.P_MOON_PRIVATE_IP_BASE
        return base_ip
    except IOError:
        print ERROR_204


def check_serial(serial):
    """check_serial validates the serial number provided by the user is valid
    and within the specified limts"""
    try:
        serial = int(serial)
    except ValueError:
        print "\nProvide an integer SCU Serial Number between 1 to 65535"
        sys.exit(ERROR_201)
    if ((serial == 0) or (serial > 65535) or (serial < 0)):
        valid_serial = 1
        print ERROR_202
        return serial, valid_serial 
    else:
        valid_serial = 0
        return serial, valid_serial


def check_channel(channel):
    """check_channel verifies the user input with the desired expected
    channel values."""
    if ((channel == 'A') or (channel == 'B') or (channel == 'G')):
        valid_channel = 0
        return channel, valid_channel
    else:
        valid_channel = 1
        print ERROR_203
        return channel, valid_channel

if __name__ == '__main__':
    main()
