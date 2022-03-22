#variables

from db_credentials import *
from sql_queries import *

import mysql.connector as msql
import requests
# methods
from etl import etl_process

def main():
  print('starting etl')
  #target_cnx=mysql.connector.connect(**datawarehouse_db_config)
  conn=msql.connect(host=datawarehouse_db_config['host_config'],user=datawarehouse_db_config['user_config'],password=datawarehouse_db_config['password_config'])
  if conn.is_connected():
    print("target db connection successful")
  else:
    return 'Error! unrecognised db platform'
  req=requests.get(api_config[0]["url"])
  if req.status_code==200:
    print("source api connection successful")
  else:
    return "Error! connecting to api"

  etl_process(insert_query, conn, req)

  

  
    



if __name__ == "__main__":
  main()