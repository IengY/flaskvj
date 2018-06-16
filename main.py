from flask import Flask
from flask import request
from submit import submitMain
app=Flask(__name__)

@app.route("/submit",methods=["POST"])
def submit():
    #print(request.args.get("problemid"))
    return submitMain.submit(request.form)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)