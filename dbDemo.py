# import mysql.connector
#
# conn = mysql.connector.connect(host='localhost',database='PythonAutomation',user='root',password='Katasraj111#')
#
# print(conn.is_connected())

from utilities.configurations import *
conn = getConnection()

cur = conn.cursor()
cur.execute('select * from CustomerInfo')
rowAll = list(cur.fetchall())
print(rowAll)

amount_sum = 0

for r in rowAll:
    amount_sum = amount_sum+r[2]

print("Sum of amount: ",amount_sum)
assert amount_sum == 340

update_query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")

cur.execute(update_query,data)
conn.commit()

conn.close()