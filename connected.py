import pymysql
conn= pymysql.connect(host='Annu',user='Annu',password='2668',db='first')
a = conn.cursor()
sql = 'SELECT*from';
a.excute(sql)

countroew = a.execute(sql)
print("number of rows :",countrow)
data = a.fetchall()
print(data)
