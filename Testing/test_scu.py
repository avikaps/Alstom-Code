import pytest
from moon_installer_v1_draft_test_release import read_FRAM
from moon_installer_v1_draft_test_release import write_FRAM
import os

from conftest import DOWNLOAD_FILE_PATH
from conftest import UPLOAD_FILE_PATH


def test_read_FRAM_CRC_A():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '1234'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_1234_Board_A_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	

def test_read_FRAM_GID_A():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '2345'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_2345_Board_A_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size
	
#gid in small letter
def test_read_FRAM_gid_A():
    hostIP = '10.107.11.184'
    memoryType = 'gid'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '2346'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_2346_Board_A_gid.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size

	
def test_read_FRAM_FUSE_A():
    hostIP = '10.107.11.184'
    memoryType = 'FUSE'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '65535'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_65535_Board_A_FUSE.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 148 == statinfo.st_size

	
def test_read_FRAM_CRC_B():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '1'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_1_Board_B_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	

def test_read_FRAM_GID_B():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '345'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_345_Board_B_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size

	
def test_read_FRAM_FUSE_B():
    hostIP = '10.107.11.184'
    memoryType = 'FUSE'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '6553'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_6553_Board_B_FUSE.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    print statinfo.st_size
    assert 148 == statinfo.st_size
	

#write and read
def test_write_read_FRAM_CRC_A():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_A_CRC.bin")
    boardType = 'A'
    serial = '45'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_45_Board_A_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content
	

def test_write_read_FRAM_GID_A():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_A_GID.bin")
    boardType = 'A'
    serial = '46'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_46_Board_A_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size

    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content

	
def test_write_read_FRAM_FUSE_A():
    hostIP = '10.107.11.184'
    memoryType = 'FUSE'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_A_FUSE.bin")
    boardType = 'A'
    serial = '47'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_47_Board_A_FUSE.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 148 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content


def test_write_read_FRAM_CRC_B():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_B_CRC.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '48'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_48_Board_B_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content
	

def test_write_read_FRAM_GID_B():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_B_GID.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '49'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_49_Board_B_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content


def test_write_read_FRAM_FUSE_B():
    hostIP = '10.107.11.184'
    memoryType = 'FUSE'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_1234_Board_B_FUSE.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '50'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_50_Board_B_FUSE.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 148 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content


#Wrong Board type
def test_read_FRAM_CRC_G():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'G'
    serial = '70'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_70_Board_G_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    if expected_file_name in files:
        file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
        statinfo = os.stat(file_name)
        assert 16 != statinfo.st_size

	
def test_read_FRAM_GID_G():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'G'
    serial = '71'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_71_Board_G_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    if expected_file_name in files:
        file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
        statinfo = os.stat(file_name)
        assert 4 != statinfo.st_size


def test_read_FRAM_FUSE_G():
    hostIP = '10.107.11.184'
    memoryType = 'FUSE'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'G'
    serial = '72'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_72_Board_G_FUSE.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    if expected_file_name in files:
        file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
        statinfo = os.stat(file_name)
        assert 148 != statinfo.st_size


#providing wrong memory type and only reading
def test_read_FRAM_ARC_A():
    hostIP = '10.107.11.184'
    memoryType = 'ARC'
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '23'

    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_23_Board_A_ARC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert (16 != statinfo.st_size and 4 != statinfo.st_size and 148 != statinfo.st_size)


#with wrong memory type, first writing then then reading. Write should not perform, but seems writing
def test_write_read_FRAM_DID_B():
    hostIP = '10.107.11.184'
    memoryType = 'DID'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_23_Board_B_DID.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '24'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_24_Board_B_DID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert (16 != statinfo.st_size and 4 != statinfo.st_size and 148 != statinfo.st_size)


#writing less size data and reading again
def test_write_read_FRAM_CRC_A1():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_23_Board_A_CRC.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '23'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_23_Board_A_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content[:9] #9 bytes written with write_FRAM()
		
		
#writing more size data and reading again	
def test_write_read_FRAM_GID_B1():
    hostIP = '10.107.11.184'
    memoryType = 'GID'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_23_Board_B_GID.bin")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'B'
    serial = '23'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_23_Board_B_GID.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 4 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content[:4] == content

		
#wrong input file extension type
def test_write_read_FRAM_CRC_A2():
    hostIP = '10.107.11.184'
    memoryType = 'CRC'
    upload_file_name = os.path.join(UPLOAD_FILE_PATH, "SCU_25_Board_A_CRC.bin")
    upload_file_name1 = os.path.join(UPLOAD_FILE_PATH, "SCU_25_Board_A_CRC.txt")
    #outPath = "D:\Data\MOON_PyTest\code\download"
    boardType = 'A'
    serial = '25'
    upload_content = None

    with open(upload_file_name, 'r') as upload_file:
		upload_content = upload_file.read()
	
    write_FRAM(hostIP, upload_file_name, memoryType, boardType)
    write_FRAM(hostIP, upload_file_name1, memoryType, boardType)
    read_FRAM(hostIP, DOWNLOAD_FILE_PATH, memoryType, boardType, serial)

    expected_file_name = "SCU_25_Board_A_CRC.bin"
    files = os.listdir(DOWNLOAD_FILE_PATH)
    #print files
    assert expected_file_name in files
    #assert "SCU_1234_Board_A_CRC.txt" in files
    file_name = os.path.join(DOWNLOAD_FILE_PATH, expected_file_name)
    statinfo = os.stat(file_name)
    #print statinfo.st_size
    assert 16 == statinfo.st_size
	
    with open(file_name, 'r') as file_content:
		content = file_content.read()
		assert upload_content == content #content should not equal to first upload file as it was .bin