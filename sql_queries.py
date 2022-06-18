#Extract and Insert queries in MySQL
#mysql_extract = ('''
#  SELECT mysql_column_1, mysql_column_2, mysql_column_3
#  FROM mysql_table
#''')


insert_query = ('''
  INSERT INTO staging.food (item_id, time, location)
  VALUES (%s, %s, %s)  
''')
# insert into table cuboids



