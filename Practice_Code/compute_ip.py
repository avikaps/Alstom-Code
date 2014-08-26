import imp
import sys

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
        print base_ip
        print type(base_ip)
        byte_1 = ((base_ip.split('.', 1))[0])
        if channel == 'A':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 2)
            # print "IP of Channel A is : ", ip_channel_a
            ip_channel_a = byte_1 + '.' + byte_2 + '.' + byte_3 + '.' + byte_4
            return ip_channel_a
        if channel == 'B':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 3)
            # print "IP of Channel B is : ", ip_channel_b
            ip_channel_b = byte_1 + '.' + byte_2 + '.' + byte_3 + '.' + byte_4
            return ip_channel_b
        if channel == 'G':
            byte_2 = str((int((base_ip.split('.', 1))[1]) & 0xFC) | 1)
            # print "IP of Gateway is : ", ip_gateway
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
    
for i in range(1,65535):
    print i
    ip_channel_a = compute_ip(i, 'A')
    ip_channel_b = compute_ip(i, 'B')
    ip_gateway = compute_ip(i, 'G')

    print ip_gateway, ip_channel_b, ip_channel_a
