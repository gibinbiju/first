#Fetch data from database
from db1 import *
db=get_connection()
cursor=db.cursor()
try:
    cursor.execute("SELECT * FROM EMPLOYEE")
    result=cursor.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print(e.args)
finally:
    db.close()