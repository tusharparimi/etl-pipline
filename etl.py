import requests
import json 
import pandas as pd


def etl(query, source_cnx, target_cnx):
    print("etl",query)
    source_dict = json.loads(source_cnx.text)
    df_nested_list = pd.json_normalize(source_dict, record_path=['cuboids'])
    print(df_nested_list)
    #print(source_dict)
    #source_string = json.dumps(source_dict,indent=2)
    #print(source_string)
    #df = pd.DataFrame.from_dict(df_nested_list, orient="index")
    #df.to_csv("C:\\Users\\tusha\\OneDrive\\Desktop\\MPS_Alalytics\\json_csv.csv",index=None)
    #print(df)
    df_nested_list.rename(columns={'position.x': 'positionx', 'position.y': 'positiony','position.z': 'positionz'}, inplace=True)
    df_nested_list.rename(columns={'dimensions.x': 'dimensionx', 'dimensions.y': 'dimensiony', 'dimensions.z': 'dimensionz'},inplace=True)
    print(df_nested_list.columns)
    cursor=target_cnx.cursor()
    #df_nested_list.to_sql(name='cuboids', con=target_cnx,schema='target', if_exists='append', index=False)
    #print("inserted")
    for i in query:
        if i=='INSERT':
            for row in df_nested_list.iterrows():
                #print(row)
                print(type(row))
                sql='''INSERT INTO target.{} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''.format(query[i])
                print(sql)
                #print(tuple(row))

                #print(list(row))
                cursor.execute(sql,row)

                target_cnx.commit()
                cursor.close()
                target_cnx.close()
       

def etl_process(queries, conn, req):
    source_cnx=req
    target_cnx=conn
    print("etl_process", queries)
  
    # loop through sql queries

    etl(queries, source_cnx, target_cnx)
    
    # close the source db connection
    source_cnx.close()