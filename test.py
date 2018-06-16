import requests
"""
{
    "oj":"pok|cf|...",
    "problemid":"1000",
    "language":"语言代号",
    "code":"代码",
}
"""
data={
    "oj":"poj",
    "problemid":"1000",
    "language":"4",
    "code":"#include<iostream> using namespace std;int main(){return 0;}"
}
base="http://127.0.0.1:5000/"
ret=requests.post(base+"submit",data=data)
print(ret.text)