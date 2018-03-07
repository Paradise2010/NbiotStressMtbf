import zipfile
import os
import re
import csv
#global parameters

testCaseNum = 0
testAttachSucc = 0
testAttachFail = 0
testCGATTSucc = 0
testCGATTFail = 0
testPingFail = 0
resetNumber = 0


def print_info(archive_name):
    global testCaseNum
    global testAttachFail
    global testAttachSucc
    global testCGATTSucc
    global resetNumber
    
   
    testCaseNum +=1
   
    zf = zipfile.ZipFile(archive_name)
    for info in zf.namelist():
        #print(info)
        if is_txtfile(info) :
            tempTxtFile = os.path.join(archive_name,info)
            print(tempTxtFile)
            with zf.open(info) as tempfile:
                for line in tempfile:
                    lineStr = line.decode()
                    #print(type(lineStr))
                    if lineStr.find('N1') != -1:
                        print("reset evb board")
                        resetNumber = resetNumber + 1
                    if lineStr.find('+CGATT: 1') != -1:
                        
                        print("Attach success")
                        testAttachSucc = testAttachSucc + 1  #attach success ,then for break
                        
                    if lineStr.find('+EGACT:1,1,1,1') != -1:
                            print("AP and MODEM tunnel active success")
                            testCGATTSucc = testCGATTSucc +1 # AP and modem tunnel acitvate success
                        
                    if lineStr.find('*MENGINFOSC:') != -1:
                        text_r = open('pci.csv').read()
                        text_a = open('pci.csv', 'a+')

                        if text_r != '':
                            text_a.write(lineStr)
                            text_a.close()

                        else:
                            text_a.write(lineStr)
                            text_a.close()

                    #print(line) 
    #if testCaseNum ==1 :
    #    os._exit(0)
def list_files(pathName):
    listfile = os.listdir(pathName)
    
    csvfile = open('mtbf.csv','w',newline='')
    spamwriter = csv.writer(csvfile,dialect='excel')
    spamwriter.writerow(["Time","AttachSucc","EGACTTSucc"])
    #print(pathName)
    for sigleFile in listfile:
        #print(sigleFile)
        fulldirfile = os.path.join(pathName,sigleFile)
        #print(fulldirfile)
        if zipfile.is_zipfile(fulldirfile):
            print_info(fulldirfile)
            spamwriter.writerow([getTimeFlag(fulldirfile),testAttachSucc,testCGATTSucc])
    csvfile.close()
def is_txtfile(fileName):
    if fileName.find('txt') == -1:
        return False
    else:
        return True

def getTimeFlag(filename):
    print("enter get time flag")
    p=re.compile(r"\d{8}_\d{6}")
    m=p.search(filename)
    return str(m.group(0))
def summary_result(filename):
    with open(filename) as f:
        for line in f:
            if line.find('+CGATT: 1'):
                print("Attach success")

if __name__ == '__main__':
   #list_files('\\\\172.28.231.42\\d$\\NB-IoT_MTBF\\Test_Result\\1201\\Results_00005')
   listdir=['\\\\172.28.231.19\\d$\\2_testResult\\20180103\\Results_00092',
   '\\\\172.28.231.21\\d$\\4_testResult\\1231\\Results_00065',
   '\\\\172.28.231.25\\d$\\2_testResult\\1231\\Results_00053',
   '\\\\172.28.231.36\\d$\\2_TestResult\\20180103\\Results_00061',
   '\\\\172.28.231.37\\d$\\2_testResult\\20181003\\Results_00069']
   for strs in listdir:
      list_files(strs)
   print("Total test case: %d" % testCaseNum)
   print("Attach success: %d" % testAttachSucc)
   print("CGATT success: %d" % testCGATTSucc)
   print("reset Number: %d" % resetNumber)  