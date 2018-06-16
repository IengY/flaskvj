from requests import Session
import passconfig
from query import pojQuery
import base64


def login(username,password):
    login_url = "http://poj.org/login"
    s = Session()
    data={
        "user_id1":username,
        "password1":password,
        "B1":"login",
        "url":"/",
    }
    s.post(login_url,data=data)
    return s
def pojsubmit(args):
    submit_url="http://poj.org/submit"
    #print(passconfig.passconfig['poj']['username'])
    username = passconfig.passconfig['poj']['username']
    password= passconfig.passconfig['poj']['password']
    s=login(username,password)
    problemID=args.get("problemid")
    language=args.get("language")
    #print(args.get('code'))
    code=str(args.get("code")).encode("utf-8")
    code=base64.b64encode(code)
    #base64.b64encode(s=,altchars=)
    data={
        "problem_id":problemID,
        "language":language,
        "source":code,
        "submit":"Submit",
        "encoded":"1"
    }
    s.post(submit_url,data=data)
    s.close()
    runID=pojQuery.getTopRunID(problemID)
    return runID
if __name__=="__main__":
    args={
        "problemid":"1000",
        "language":"4",
        "code":"#include<iostream> using namespace std;int main(){return 0;}"
    }
    ret=pojsubmit(args)
    print(ret)