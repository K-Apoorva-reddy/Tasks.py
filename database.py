import mysql.connector
from db import info

try:
    mysql.connector.connect (**info)
    print('connection successful')
except:
    print('not able to connect')
      # this is index.py file 
      # output:- 
      # connection successful 
info={
    'user':'root',
    'password':'deepu@0811',
    'host':'localhost',
    'port':3306
}
    # this is db.py file 
pdbc python
