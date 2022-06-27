import requests

class RequestData:
    def hello(self):
        res=requests.get('http://127.0.0.1:5000/') 
        print(res.text)
        print(res.status_code) 

data=RequestData()
data.hello()



