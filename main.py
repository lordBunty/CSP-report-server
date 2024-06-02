import tempfile, app, os, timestamp, tempfile

dir = r'./cpsReport'+timestamp.timestamp()+'/'
os.mkdir(dir)

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    app.startServer(dir,tmpdirname)