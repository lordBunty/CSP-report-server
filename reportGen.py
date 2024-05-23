from openpyxl import Workbook, load_workbook
import timestamp

strr=['document-uri":"','referrer":"','violated-directive":"','effective-directive":"','original-policy":"','disposition":"','blocked-uri":"','line-number":','source-file":"','status-code":','script-sample":"']



def deserialize(filePath):
    try:
        text_file = open(filePath)
        data = text_file.readlines()
        text_file.close()
        return data
    except:
        print("An exception occurred while opening the file")

def wrtDataToXl(r,c,finalStr):
    try:
        sheet.cell(row=r, column=c).value = finalStr  
    except:
        print("An exception occurred while writing data to the excel")

def sort(strr,data,r):
    try:
        c=1
        for i in strr:
            finalStr=(data.rsplit(i)[1]).split('"')[0]
            wrtDataToXl(r,c,finalStr)
            c=c+1
    except:
        print("an error occured during writing data to excel")
    
    
def genReport(filePath):
    pathToCsvFile='SpreadSheet_'+timestamp.timestamp()+'.xlsx'
    wb = Workbook()
    wb.save(pathToCsvFile)
    wb = load_workbook(pathToCsvFile)
    global sheet
    sheet = wb.active
    count=2
    for i in filePath:
        data=str((deserialize(i)))
        sort(strr,data,count)
        count+=1
    wb.save(pathToCsvFile)
    return str(pathToCsvFile)