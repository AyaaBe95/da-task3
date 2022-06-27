import psycopg2
from flask import Flask ,request
import requests

 #Establishing the connection
conn = psycopg2.connect(
database="ProductsManagement", user='postgres', password='0000', host='127.0.0.1', port= '5432')

#Creating a cursor object using the cursor() method
cursor = conn.cursor() 

app = Flask(__name__)
class API:
    ### method for creating tables ###

    '''http://127.0.0.1:5000/create?tableName=products'''
    @app.route('/create')
    def create_table():
        global conn
        global cursor
        tableName=str(request.args.get('tableName'))
        try: 
            #Creating table as per requirement
            if tableName == 'products':
                sql ='CREATE TABLE if not exists ' + tableName + '''(  
                    ProductID serial, 
	                PRIMARY KEY(ProductID),
                    ProductName VARCHAR(100), 
	                ProductPrice int
                    )'''
            elif tableName == 'customers':
                sql ='CREATE TABLE if not exists ' + tableName  + '''(  
                    CustomerID serial,
	                PRIMARY KEY(CustomerID),
                    CustomerName VARCHAR(100), 
	                ContactNumber int,
                    City VARCHAR(100),  
                    Country VARCHAR(100)  
                    )'''
            elif tableName == 'orders':
                sql ='CREATE TABLE if not exists ' + tableName  + '''(  
                    OrderID serial,
                    OrderDate DATE,
                    CustomerID INT,
                    ProductID INT,
                    PRIMARY KEY(OrderID),
                    CONSTRAINT fk_customer FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
   	                CONSTRAINT fk_product FOREIGN KEY(ProductID) REFERENCES Products(ProductID)  
                    )'''
            else:
                print('not valid table name')
            cursor.execute(sql,(tableName,))
            conn.commit()
            return tableName + '\' table created successfully'

        except (Exception, psycopg2.Error) as error:
            return "Failed to create "+ tableName, error

        finally:
            # closing database connection.
            if conn:
                cursor.close()
                conn.close()

    ### methods for inserting data into tables ###

    '''http://127.0.0.1:5000/addProduct?ProductName=ddd&ProductPrice=60'''
    @app.route('/addProduct',methods=['POST'])
    def insert_product():
        global conn
        global cursor
        ProductName=str(request.args.get('ProductName'))
        ProductPrice=int(request.args.get('ProductPrice'))

        sql = """INSERT INTO Products(ProductName,ProductPrice)
                 VALUES(%s,%s) RETURNING ProductID;"""
        ProductID = None
        try:
            cursor.execute(sql, (ProductName,ProductPrice,))
            # get the generated id back
            ProductID = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            return "Failed to insert product ", error

        finally:
            if conn:
                cursor.close()
                conn.close()
        return ProductName + ' inserted successfully into products\' table'
    
    '''http://127.0.0.1:5000/addCustomer?CustomerName=ahmad&ContactNumber=666&Country=Jordan&City=Irbid'''
    @app.route('/addCustomer',methods=['POST'])
    def insert_customer():
        global conn
        global cursor
        CustomerName=str(request.args.get('CustomerName'))
        ContactNumber=int(request.args.get('ContactNumber'))
        Country=str(request.args.get('Country'))
        City=str(request.args.get('City'))

        sql = """INSERT INTO Customers(CustomerName,ContactNumber,Country,City)
                 VALUES(%s,%s,%s,%s) RETURNING CustomerID;"""
        CustomerID = None
        try:
            cursor.execute(sql, (CustomerName,ContactNumber,Country,City))
            # get the generated id back
            CustomerID = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            return "Failed to insert customer ", error

        finally:
            if conn:
                cursor.close()
                conn.close()
        return CustomerName + ' inserted successfully into customers\' table'
    
    '''http://127.0.0.1:5000/createOrder?OrderDate=2022-06-04&CustomerID=1&ProductID=1'''
    @app.route('/createOrder',methods=['POST'])
    def create_order():
        global conn
        global cursor
        OrderDate=str(request.args.get('OrderDate'))
        CustomerID=int(request.args.get('CustomerID'))
        ProductID=int(request.args.get('ProductID'))

        sql = """INSERT INTO Orders(OrderDate,CustomerID,ProductID)
                 VALUES(%s,%s,%s) RETURNING OrderID;"""
        OrderID = None
        try:
            cursor.execute(sql, (OrderDate,CustomerID,ProductID))
            # get the generated id back
            OrderID = cursor.fetchone()[0]
            conn.commit()
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            return "Failed to create order ", error

        finally:
            if conn:
                cursor.close()
                conn.close()
        return 'Order '+ str(OrderID) + ' created successfully'

if __name__=="__main__":
    app.run(debug=True)

api=API()
api.create_table
#api.insert_product
#api.insert_customer
