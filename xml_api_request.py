import mysql.connector
import requests
import xml.etree.ElementTree as ET
def db_connection():
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai@2349",
    database="target"
    )
    if conn.is_connected():
        print("target db connection successful")
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
    data='''<?xml version="1.0" encoding="UTF-8"?>
    <metadata>
    <food>
        <item name="breakfast">Idly</item>
        <price>$2.5</price>
        <description>
       Two idly's with chutney
       </description>
        <calories>553</calories>
    </food>
    <food>
        <item name="breakfast">Idlys</item>
        <price>$2.5</price>
        <description>
       Two idly's with chutney
       </description>
        <calories>553</calories>
    </food>
    </metadata>
    '''
    myroot = ET.fromstring(data)
    print(myroot[0].tag)
    print(myroot[0].attrib)
    print(myroot[0].text)
    temp=[]
    for i in myroot:
        for x in i:
            print(x.text)
            temp.append(x.text)
        ins_string='INSERT INTO food VALUES(%s, %s, %s, %s)'
        val = (temp[0], temp[1],temp[2], temp[3])
        insert(ins_string,val)
        temp=[]
        
        
        
api_request()
