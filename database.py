import mysql.connector
info = {
    'user':'root',
    'password':'Apoorva@28',
    'host':'localhost',
    'port':'3306'
}

try:
    mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')