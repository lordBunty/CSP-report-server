from flask import Flask, request 
from flask import send_file
import reportGen, timestamp


jsonFileList=[]


app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def foo():
    if request.method=='GET':
        return '<form action="/report" method="get"><button type="submit">Generate Report</button>'
        
        
    elif request.method=='POST':
        global jsonfileList
        path= str(dirr)+'reprot_'+timestamp.timestamp()+'.json'
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
        pathtocsvfile=reportGen.genReport(jsonFileList,tmpdir)
        return send_file(pathtocsvfile, as_attachment=True)

    except:
        return 'an error occured while exporting'
    
def startServer(dir,tmpdirname):
    global dirr, tmpdir
    dirr=dir
    tmpdir=tmpdirname
    app.run(host='0.0.0.0',port=80)
