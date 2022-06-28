import requests

class RequestData:
    '''Creating tables'''

    def createProductsTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)}) 
        print(res.text) 
        print(res.status_code)   
    
    def createCustomersTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)})  
        print(res.text) 
        print(res.status_code) 
    
    def createOrdersTable(self,tableName):
        res = requests.get('http://127.0.0.1:5000/create',params={'tableName':str(tableName)})  
        print(res.text) 
        print(res.status_code)  

    '''Inserting into tables'''

    def addProduct(self,productName,productPrice):
        res=requests.post('http://127.0.0.1:5000/addProduct',params={'ProductName':str(productName),'ProductPrice':int(productPrice)})
        print(res.text)
        print(res.status_code)

    def addCustomer(self,CustomerName,ContactNumber,Country,City):
        res=requests.post('http://127.0.0.1:5000/addCustomer',params={'CustomerName':str(CustomerName),
        'ContactNumber':int(ContactNumber),'Country':str(Country),'City':str(City)})
        print(res.text)
        print(res.status_code)

    def createOrder(self,OrderDate,CustomerID,ProductID):
        res=requests.post('http://127.0.0.1:5000/createOrder',params={'OrderDate':str(OrderDate),
        'CustomerID':int(CustomerID),'ProductID':int(ProductID)})
        print(res.text)
        print(res.status_code)
    
    '''get data from tables'''

    def getData(self,tableName):
        res = requests.get('http://127.0.0.1:5000/get',params={'tableName':str(tableName)})  
        print(res.text)
        print(res.status_code) 
    
    '''delete data from tables'''
    def delete(self,tableName,id):
        res = requests.get('http://127.0.0.1:5000/delete',params={'tableName':str(tableName),'id':int(id)})  
        print(res.text)
        print(res.status_code) 
    
    ''' update data '''
    def update_product(self,productName,productPrice,productID):
        res = requests.get('http://127.0.0.1:5000/updateProduct',params={'ProductName':str(productName),
        'ProductPrice':int(productPrice),'ProductID':int(productID)})  
        print(res.text)
        print(res.status_code) 
    
    def update_customer(self,CustomerName,ContactNumber,Country,City,CustomerID):
        res = requests.get('http://127.0.0.1:5000/updateCustomer',params={'CustomerName':str(CustomerName),
        'ContactNumber':int(ContactNumber),'Country':str(Country),'City':str(City),'CustomerID':int(CustomerID)})  
        print(res.text)
        print(res.status_code)

    def update_order(self,OrderDate,CustomerID,ProductID,OrderID):
        res = requests.get('http://127.0.0.1:5000/updateOrder',params={'OrderDate':str(OrderDate),
        'CustomerID':int(CustomerID),'ProductID':int(ProductID),'OrderID':int(OrderID)})  
        print(res.text)
        print(res.status_code) 
    
    '''join tables'''
    def join_tables(self,table1,table2,table3):
        res = requests.get('http://127.0.0.1:5000/getData',params={'table1':str(table1),
        'table2':str(table2),'table3':str(table3)})  
        print(res.text)
        print(res.status_code) 

data=RequestData()

'''create tables'''
#data.createOrdersTable('products')
#data.createOrdersTable('customers')
#data.createOrdersTable('orders')

'''insert into tables'''
#data.addProduct('glass3',20)
#data.addCustomer('Moh',79999,'Jordan','Irbid')
#data.createOrder('2022-06-04',1,7)

'''get data from tables'''
#data.getData('products')
#data.getData('customers')
#data.getData('orders')

'''delete data from tables'''
#data.delete('products',1)
#data.delete('customers',1)
#data.delete('orders',1)

'''Update data '''
#data.update_product('glass',25,1)
#data.update_customer('Huda',999,'Jordan','Irbid',1)
#data.update_order('2022-06-15',1,2,1)

'''Join data'''
#data.join_tables('Customers','Orders','Products')


