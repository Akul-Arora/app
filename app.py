from flask import Flask,jsonify,Request
from flask.json import jsonify
from flask.wrappers import Request
from werkzeug.wrappers import request 
app=Flask(__name__)
tasks=[
{
    "id":1,
    "title": u"watch movie",
    "description":u"twilight,new moon,eclipse",
    "done":False
},
{
 "id":2,   
 "title":u"play games",
 "description":u"ludo,snakes and ladders,sequence",
 "done":False
}

]

@app.route("/")
def hello_world():
    return "Hello World!!!!"

@app.route("/add-data",methods=["POST"])
def addingtask():
    if not request.json:
        return jsonify({'status':'error',
        "message":"please provide valid data"},400)

    task={'id':tasks[-1]['id']+1,
    'title':request.json['title'],
    'description':request.json.get('description',""),
    'done':False
    }    
    tasks.append(task)
    return jsonify({
        'status':'success',
        "message":"task is added succesfully"})
        
            
@app.route("/get-data")
def gettask():
    return jsonify({"data":tasks})



if(__name__ == "__main__"):
    app.run(debug=True)