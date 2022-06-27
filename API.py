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
    '''http://127.0.0.1:5000/'''
    @app.route('/')
    def insert_product():
        return 'hello'

if __name__=="__main__":
    app.run(debug=True)

api=API()


