#variables

from db_credentials import *
from sql_queries import *

import mysql.connector 
import requests
from etl import etl_process


  
def db_connection():  
  print('starting etl')
  conn=mysql.connector.connect(host=datawarehouse_db_config['host_config']
                    ,user=datawarehouse_db_config['user_config']
                    ,password=datawarehouse_db_config['password_config']
                   )
  if conn.is_connected():
    print("target db connection successful")
    return conn
  else:
    return 'error! unrecognised db platform'
  
  
  
  
def api_connection():    
  api_request=requests.get(api_config[0]["url"])
  if api_request.status_code==200:
    print("source api connection successful")
    return api_request
  else:
    return "error! connecting to api"
  
  
      
      
def main():
  db_conn = db_connection()
  api_conn = api_connection()
  if 'error' not in db_conn & 'error' not in api_conn: 
    etl_process(load_query, db_conn, api_conn)
  else:
    'error!'

  

  
   
if __name__ == "__main__":
  main()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
