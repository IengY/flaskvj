# flaskvj
使用此模块可以很方便的搭建出一个供vj使用的api服务器，提供交题，查询结果，获取题面等功能。

## 如何使用
配置passconfig.py，填写对应的oj账号密码，然后按下两种方法之一运行
* 安装python3，以及flask、bs4、requests库,运行main.py程序，自行使用nginx等工具进行配置.
* 拷贝dockerfile到上层目录,构建之后运行.

## API
### submit
url     : /submit\
method  : POST\
request :
```json
{
    "oj":"oj名称",
    "problemid":"题号",
    "language":"对应语言",
    "code":"代码"
}
```
response:
```json
{
        "status":200,
        "data":{
            "runid":"运行编号|提交编号",
            "info":"对应信息|空"
        }
}
```

