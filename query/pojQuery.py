import requests
from bs4 import BeautifulSoup
import passconfig

query_url = "http://poj.org/status"
def queryStatus(problemID,RunID):
    username = passconfig.passconfig['poj']['username']
    data = {
        "problem_id": problemID,
        "user_id": username,
    }
    page = requests.get(query_url, params=data)
    soup = BeautifulSoup(page.text, "html.parser")
    ceinfo_url="http://poj.org/showcompileinfo"
    st = soup.find(attrs={"class": "a"}).find_all('tr')[1:]
    ret={
        "result":"unknown",
        "info":"error",
    }
    for status in st:
        temp=status.find_all('td')
        runid=temp[0].text
        result=temp[3]
        if(runid==RunID):
            if result.text=="Compile Error":
                ceinfo_page=requests.get(ceinfo_url,params={"solution_id":RunID})
                ceinfo_soup=BeautifulSoup(ceinfo_page.text,"html.parser")
                ret['info']=ceinfo_soup.find('pre').text
            ret['result']=result.text
    return ret
def getTopRunID(problemID):
    username= passconfig.passconfig['poj']['username']
    data={
        "problem_id":problemID,
        "user_id":username
    }
    #print(data)
    page=requests.get(query_url,params=data)
    soup=BeautifulSoup(page.text,"html.parser")
    #print(page.text)
    runid=soup.find(attrs={"class":"a"}).find_all("tr")[1].find('td').text
    return runid
if __name__=="__main__":
    print(queryStatus("1000","18699713"))