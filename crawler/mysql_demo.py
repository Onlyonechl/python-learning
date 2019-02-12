
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql_demo',port=3306)

cursor = conn.cursor()

sql = """
insert into user(id,username,age,password) values (null,%s,%s,%s)
"""
username = 'ccc'
age = 21
password = '111111'

cursor.execute(sql,(username,age,password))

conn.commit()
conn.close()