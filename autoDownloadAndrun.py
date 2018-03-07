#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os
import os.path
import shutil
import zipfile

import win32gui
import win32com
import win32com.client
import pythoncom
import win32process
import win32event

# search nbiot latest load from \\mshhfs09\DZ_Build_Image\@DZ_Build_Image\multi_repos\geneva-mp-mp3-nbiot
def searchLatestLoad():
    path = "//mshhfs09/DZ_Build_Image/@DZ_Build_Image/multi_repos/geneva-mp-mp3-nbiot/"
    fileList = os.listdir(path)
    try: 
        #fo = open("\\mshhfs09\DZ_Build_Image\@DZ_Build_Image\multi_repos\geneva-mp-mp3-nbiot\")
        fileList.sort(key=lambda fn: os.path.getmtime(path+fn))
        return os.path.join(path,fileList[-1])
    except:    
        return 0

def copyFile(sourceFile):
    file_dir="D:\\test_load"
    # erase all of files in file_dir
    if os.path.exists(file_dir):
        print "test_load existed!!!!"
        shutil.rmtree(file_dir)
    os.mkdir(file_dir)
    
    shutil.copy(sourceFile,file_dir)

def readyZipFile(zipFileNamePath):
    # win zip file to target directory, then invoke autodown function
    readyTestLoad = os.listdir(zipFileNamePath)
    zipFile = zipfile.ZipFile(zipFileNamePath+"\\"+readyTestLoad[0])
    if not zipfile.is_zipfile(zipFileNamePath+"\\"+readyTestLoad[0]):
        return False
    print zipFile.filename
    for file in zipFile.namelist():
        zipFile.extract(file, zipFileNamePath)
    zipFile.close()
def run(interval):
    # execute one action  at certain time
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval-time.time()%interval
            time.sleep(time_remaining)
            doWork()
        except Exception as e:
            print (e)
def getCFGFile(projectName):
    targetDirecotory = "D:\\test_load" + "\\" + projectName
    for cfgFile in os.listdir(targetDirecotory):
        if cfgFile == "flash_download.cfg":
            return targetDirecotory+os.sep+cfgFile


def RunProceWaitExit( procPara ):

    #if not os.path.isfile(procPara):
     #   return -1
    teratermLocation='C:\\Program Files (x86)\\teraterm\\ttermpro.exe'
    commandLine=teratermLocation+" "+procPara
    handle=win32process.CreateProcess( None,
     commandLine , 
     None , 
     None , 
     0 ,
     win32process.CREATE_NEW_CONSOLE , 
     None , 
     None ,
     win32process.STARTUPINFO())

    win32event.WaitForSingleObject(handle[0], -1)


def executeDownload():
    return 0

if __name__ == "__main__":
    print searchLatestLoad()
    copyFile(searchLatestLoad())
    readyZipFile("D:\\test_load")
    print getCFGFile("nbiot_m2m_demo")