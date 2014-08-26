import pytest
from moon_installer_4 import compute_ip

def test_compute_valid_ip_A():
	computedip = compute_ip(12345, 'A')
	#print "Ip computed with serail no 12345 and channel A is"
	#print computedip
	expectedip = "10.48.57.2"
	assert expectedip == computedip
	
def test_compute_valid_ip_A1():
	computedip = compute_ip(1, 'A')
	assert "10.0.1.2" == computedip
	
def test_compute_valid_ip_A65535():
	computedip = compute_ip(65535, 'A')
	assert "10.255.255.2" == computedip
	
def test_compute_valid_ip_B():
	computedip = compute_ip(65500, 'B')
	#print "Ip computed with serail no 65500 and channel B is"
	#print computedip
	expectedip = "10.255.220.3"
	assert expectedip == computedip
	
def test_compute_valid_ip_B1():
	computedip = compute_ip(1, 'B')
	assert "10.0.1.3" == computedip
	
def test_compute_valid_ip_B65535():
	computedip = compute_ip(65535, 'B')
	assert "10.255.255.3" == computedip
	
def test_compute_valid_ip_G():
	computedip = compute_ip(1, 'G')
	#print "Ip computed with serail no 1 and channel G is"
	#print computedip
	expectedip = "10.0.1.1"
	assert expectedip == computedip
	
def test_compute_valid_ip_G1():
	computedip = compute_ip(1, 'G')
	assert "10.0.1.1" == computedip
	
def test_compute_valid_ip_G65535():
	computedip = compute_ip(65535, 'G')
	assert "10.255.255.1" == computedip
	
def test_compute_valid_ip_g255():
	computedip = compute_ip(255, 'g')
	assert "10.0.255.1" == computedip
	
def test_compute_invalid_ip_serial_beyond():
	computedip = compute_ip(65536, 'A')
	assert None == computedip
	computedip = compute_ip(65550, 'B')
	assert None == computedip
	computedip = compute_ip(76543, 'G')
	assert None == computedip
	
def test_compute_invalid_ip_serial_0():
	computedip = compute_ip(0, 'A')
	assert None == computedip
	computedip = compute_ip(0, 'B')
	assert None == computedip
	computedip = compute_ip(0, 'G')
	assert None == computedip
	
def test_compute_valid_ip_A2():
	computedip = compute_ip(2, 'A')
	assert "10.0.2.2" == computedip
	
def test_compute_invalid_ip_channelC():
	computedip = compute_ip(10, 'C')
	assert None == computedip
	
def test_compute_invalid_ip_serial0_channelK():
	computedip = compute_ip(0, 'K')
	assert None == computedip
	
def test_compute_invalid_ip_serial65537_channelZ():
	computedip = compute_ip(65537, 'Z')
	assert None == computedip
	
def test_compute_invalid_ip_serial_1_A():
	computedip = compute_ip(-1, 'A')
	assert None == computedip

