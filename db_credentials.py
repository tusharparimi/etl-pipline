datawarehouse_name = 'target'

#mysql (target db, datawarehouse)
datawarehouse_db_config={
    'user_config': 'root',
    'password_config': '******',
    'host_config': 'localhost',
    'database_config': 'target',
}

# API (source json)
api_config = [
  {
    'url': 'https://scaleapi-results.s3.us-west-1.amazonaws.com/2f97ba0b-67fd-4ac5-94c0-865073aea577'
  }

]
