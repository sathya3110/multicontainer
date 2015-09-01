from flask import Flask
from flask import render_template,request
import MySQLdb
db = MySQLdb.connect(host="mysqldb", # your host, usually localhost
                     user="monty", # your username
                      passwd="monty", # your password
                      db="dummy")
            
app = Flask(__name__)
app.root_path

cur = db.cursor() 
cur.execute("SELECT * FROM devops")
rows=cur.fetchall()
list1=rows[0]
list2=rows[1]
list3=rows[2]


           
@app.route('/')
def showUI():
    print("here are the details")
    return render_template('s.html')

@app.route('/final')
def GetDetails():
    
    return render_template('final.html',list1=list1,list2=list2,list3=list3)


if __name__ == '__main__':
    app.debug= True;
    app.run(host='0.0.0.0')
