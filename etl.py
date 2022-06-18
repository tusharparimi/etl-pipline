import requests
import json 
import pandas as pd

    
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
            
            
            
def etl(query, source_cnx, target_cnx):
    print("etl",query)
    
    cursor=target_cnx.cursor()

    for i in query:
        if i=='INSERT':
            sql=query[i]
            cursor.execute(sql,row)
            
            target_cnx.commit()
            cursor.close()
            target_cnx.close()
       

def etl_process(queries, conn, req):
    source_cnx=req
    target_cnx=conn
    print("etl_process", queries)

    etl(queries, source_cnx, target_cnx)
    
    # close the source db connection
    source_cnx.close()
