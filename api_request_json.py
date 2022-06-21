import mysql.connector
import requests
import json


def db_connection():
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="target"
    )
    if conn.is_connected():
        #print("target db connection successful")
        return conn
    else:
        return 'Error! unrecognised db platform'
      
      
      
def insert(ins_string,val):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute(ins_string,val)
    conn.commit()
    cursor.close()
    conn.close()
    
    
    
def api_request():
    data=requests.get("https://*************************")
    print(data.status_code)
    print(type(data.text))
    print(type(data))
    print(data.headers)
    api_list=json.loads(data.text)
    print(type(api_list))
    for r1 in api_list:
        for r2 in r1["cuboids"]:
            ins_string='INSERT INTO imaging VALUES(%s, %s, %s)'
            val = (r2["position"]["x"], r2["position"]["y"],r2["position"]["z"])
            insert(ins_string,val)
            
            
            
api_request()
