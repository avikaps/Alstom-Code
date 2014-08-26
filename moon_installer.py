#!/usr/bin/env python

import optparse

prog_name = "moon_installer.py"
# usefull when the program alters from the normal python file

prog_version = "%prog 0.1 Copyright (C) 2014 ALSTOM TRANSPORT"

prog_usage = "Usage: %prog [SERVICES] [OPTION]... [REST]"

prog_desc = "Demonstrates python code for OFF-LINE Moon Installer.\
This script is supplied with some [SERVICES] and [COMMAND OPTION] related to\
each option as guided in the usage to interact with the Embedded Installer\
to give definate results "

def parse_options():
    parser = optparse.OptionParser(usage=prog_usage, version=prog_version,
                                   description=prog_desc)


    read_fuse_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')

    read_fuse_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    read_fuse_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    read_fuse_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    write_fuse_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')

    write_fuse_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    write_fuse_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    write_fuse_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)


    read_crc_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')

    read_crc_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    read_crc_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    read_crc_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    write_crc_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')

    write_crc_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    write_crc_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    write_crc_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)
    

    read_gid_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')

    read_gid_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    read_gid_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    read_gid_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    write_gid_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')
    write_gid_opts.add_option("-b", "--board-type", help="SCU board type"
                            " Eg: Channel 'A' / 'B' / 'G' ")
    write_gid_opts.add_option("-s", "--serial", help="SCU serial number"
                            " and creates an IP Address with board type")
    write_gid_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    write_gid_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    write_gid_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    write_config_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')
    write_config_opts.add_option("-b", "--board-type", help="SCU board type"
                            " Eg: Channel 'A' / 'B' / 'G' ")
    write_config_opts.add_option("-s", "--serial", help="SCU serial number"
                            " and creates an IP Address with board type")
    write_config_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    write_config_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    write_config_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)    

    format_flash_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')
    format_flash_opts.add_option("-b", "--board-type", help="SCU board type"
                            " Eg: Channel 'A' / 'B' / 'G' ")
    format_flash_opts.add_option("-s", "--serial", help="SCU serial number"
                            " and creates an IP Address with board type")
    format_flash_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    format_flash_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    format_flash_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    upload_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')
    upload_opts.add_option("-b", "--board-type", help="SCU board type"
                            " Eg: Channel 'A' / 'B' / 'G' ")
    upload_opts.add_option("-s", "--serial", help="SCU serial number"
                            " and creates an IP Address with board type")
    upload_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    upload_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    upload_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    download_opts = optparse.OptionGroup(parser, 'Read from FRAM Options ',
                                     'These options are the paramaters'
                                     'required to read fuses')
    download_opts.add_option("-b", "--board-type", help="SCU board type"
                            " Eg: Channel 'A' / 'B' / 'G' ")
    download_opts.add_option("-s", "--serial", help="SCU serial number"
                            " and creates an IP Address with board type")
    download_opts.add_option("-m", "--start-memory", help="start address"
                            " of the memory location in SCU",)
    download_opts.add_option("-e", "--end-memory", help="end address of"
                            " the memory location in SCU",)
    download_opts.add_option("-o", "--origin-path", help="path where the"
                            " file is currently located in host computer",)

    parser.add_option_group(read_fuse_opts)
    parser.add_option_group(write_fuse_opts)

    parser.add_option_group(read_crc_opts)
    parser.add_option_group(write_crc_opts)
    
    parser.add_option_group(read_gid_opts)
    parser.add_option_group(write_gid_opts)
    
    parser.add_option_group(format_flash_opts)
    parser.add_option_group(upload_opts)
    parser.add_option_group(download_opts)
    
    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.print_help()

if __name__ == '__main__':
    parse_options()
