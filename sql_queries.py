#Extract and Insert queries in MySQL
#mysql_extract = ('''
#  SELECT mysql_column_1, mysql_column_2, mysql_column_3
#  FROM mysql_table
#''')


mysql_insert = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')
# insert into table cuboids
insert_query={'INSERT':'cuboids'}


