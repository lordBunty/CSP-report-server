from flask import Flask, request 
from flask import send_file
import random, os, reportGen, timestamp

dir = r'./cpsReport'+str(random.random())+'_'+timestamp.timestamp()+'/'

os.mkdir(dir)
jsonFileList=[]


app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def foo():
    if request.method=='GET':
        return '<form action="/report" method="get"><button type="submit">Generate Report</button>'
        
        
    elif request.method=='POST':
        # global jsonfileList
        path= str(dir)+'reprot_'+str(random.random())+'_'+timestamp.timestamp()+'.json'
        data = request.get_data()
        f=open(path,'w')
        f.write(data.decode())
        f.close()
        jsonFileList.append(path)
        return 'CSP request recieved successfully'
    
    else:
        return "Method not allowed"
    

@app.route('/report')
def report():
    
    try:    
        pathtocsvfile=reportGen.genReport(jsonFileList)
        return send_file(pathtocsvfile, as_attachment=True)

    except:
        return 'an error occured while exporting'
    
    finally:
        pass

app.run(host='0.0.0.0',port=80)
