from datetime import datetime

sFilePath = "D:\\Study\\Python\\EX0629\\GRD004-621DataLog.csv"

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
    iLocDate = sText.find(",")
    dictValue["LOGTIME"] = "20"+sText[:iLocDate]

    iLocCode = sText[iLocDate+1:].find(",")
    if iLocCode == -1:
        dictValue["PROCESS"] = sText[iLocDate+1:]
        dictValue["MESSAGE"] = ""
    else:
        dictValue["PROCESS"] = sText[iLocDate+1:iLocDate+iLocCode+1]
        dictValue["MESSAGE"] = sText[iLocDate+iLocCode+2:]

    print("File = [{}], Execute Time = [{}], Machine = [{}], Log Time = [{}], Process = [{}], Message = [{}]".format(dictValue["FILENAME"],dictValue["UPLOADED_ON"],dictValue["MACHINE_NAME"],dictValue["LOGTIME"],dictValue["PROCESS"],dictValue["MESSAGE"]))