from datetime import datetime

sFilePath = "D:\\Study\\Python\\EX0629\\GRD004-621EasyLog.csv"

sFileName = sFilePath[sFilePath.rfind("\\")+1:]
sCreateTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
sMachineName = sFileName[:6]

oFile = open(sFilePath,"r")
oText = oFile.read()
oFile.close()

lsText = oText.split("\n")
lsText.pop()  #return the last element, and remove it

dictValue = dict()
dictValue["FILENAME"] = sFileName
dictValue["UPLOADED_ON"] = sCreateTime
dictValue["MACHINE_NAME"] = sMachineName

for sText in lsText:
    
    sText=sText.rstrip()
    lsElement = sText.split(",")    
    dictValue["LOGTIME"] = "20"+lsElement[1]+" "+lsElement[2]

    iCheck = sText.count(",")
    if iCheck >= 4:
        dictValue["PROCESS"] = lsElement[3]
        dictValue["MESSAGE"] = lsElement[4]
        print("File = [{}], Execute Time = [{}], Machine = [{}], Log Time = [{}], Process = [{}], Message = [{}]".format(dictValue["FILENAME"],dictValue["UPLOADED_ON"],dictValue["MACHINE_NAME"],dictValue["LOGTIME"],dictValue["PROCESS"],dictValue["MESSAGE"]))
    else:
        pass    