import pymongo
from pymongo import MongoClient
from flask import Flask, request, render_template
import base64
import time
import datetime
app = Flask(__name__)

client = MongoClient('mongodb://surendranaidu04:surendra@ds023714.mlab.com:23714/project87754')
db = client.project87754
@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/upfile')
def Welcome1():
    return render_template('uploadtxt.html')

@app.route('/searchfile')
def searchfile():
    return render_template('findfile.html')
	


	
@app.route('/uploadfile',methods=['GET','POST'])
def Uploadfile():
     if request.method=='POST':
        img1 = request.files['fileupload']
        name  = img1.filename
        file_data = img1.read()
        db.files.insert_one({"name":name ,"image" : file_data})
        return "uploaded"

@app.route('/findfile',methods=['GET','POST'])
def findfile():
    search = request.form['search']
    filesdb = db.files		
    files1  = []
    files1 = filesdb.find()
    fil1 = []
    total = 0
    for x in files1:
        temp = datetime.datetime.now()
        st = temp.microsecond
        if x['image'].find(search) > -1:
            temp = datetime.datetime.now()
            et = temp.microsecond  
            t = et-st
            total = total+int(t)
            fil1.append({"file" : x['image'],"time" : t})
    return render_template("filedisplay.html",result=fil1,time = total)
	
@app.route('/upload',methods=['GET','POST'])
def Upload():
     if request.method=='POST':
        img1 = request.files['image']
        name  = request.form['username']
        image_data = open(img1.filename,"rb").read()
        encoded_string = base64.b64encode(image_data)
        db.images.insert_one({"name":name ,"image" :  encoded_string})
        return "surendra"
		

			
if __name__ == "__main__":
    app.run(debug=True)


