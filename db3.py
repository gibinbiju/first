#Insertion into Table
from db1 import *
db=get_connection()
print(db)
cursor=db.cursor()
query="""INSERT INTO EMPLOYEE(FIRST_NAME,lAST_NAME,AGE,SEX,INCOME)
        VALUES('VIJAY','KARAN',21,'M',70000)"""
try:
    cursor.execute(query)
    print("data inserted succesfully")
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()