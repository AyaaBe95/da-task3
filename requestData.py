import requests

class RequestData:
    def createProductsTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)}) 
        print(res.text) 
        return res.status_code  
    
    def createCustomersTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)})  
        return res.status_code 
    
    def createOrdersTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)})  
        print(res.text) 
        print(res.status_code)  

data=RequestData()
#data.createOrdersTable('products')
#data.createOrdersTable('customers')
#data.createOrdersTable('orders')