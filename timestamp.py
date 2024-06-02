import datetime, random

def timestamp():
    ts= str(datetime.datetime.now())
    ts=ts.replace(' ','_')
    ts=ts.replace(':','-')
    ts=ts.replace('.','-')
    return str(random.random())+'_'+ts