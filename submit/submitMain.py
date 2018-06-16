import json
from submit import pojSubmit
def submit(args):
    #print(args)
    ret={
        "status":200,
        "data":{
            "runid":"",
            "info":"",
        }
    }
    try:
        switch={
            "poj":pojSubmit.pojsubmit(args),
        }
        ret['data']['runid']=switch[args.get('oj')]
        ret['info']="success"
    except:
        ret['status']=500
    return json.dumps(ret)
