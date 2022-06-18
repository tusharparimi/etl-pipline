import requests
import json 
import pandas as pd

    
def extract(api_conn):
    print(api_conn.headers)
    api_list=json.loads(api_conn.text)
    
    for r1 in api_list:
        for r2 in r1["cuboids"]:
            row = (r2["position"]["x"], r2["position"]["y"],r2["position"]["z"])
            return row
            
            
            
def etl(query, db_conn, api_conn):
    print("etl",query)
    
    row = extract(api_conn)
    
    cursor=db_conn.cursor()
    cursor.execute(query,row)

    api_conn.commit()
    cursor.close()
    api_conn.close()
    db_conn.close()
       

def etl_process(queries, conn, req):
    db_conn=req
    api_conn=conn
    print("etl_process", queries)

    etl(queries, db_conn, api_conn)

    
