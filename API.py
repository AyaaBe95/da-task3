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

if __name__=="__main__":
    app.run(debug=True)

api=API()
api.create_table
