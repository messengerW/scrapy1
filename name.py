import random
import pymysql

i = random.randint(0,100)
j = random.randint(0,100)

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="232624",
    database="test"
)

cusor = db.cursor()

sql1 = "SELECT word_1 FROM NAME WHERE no = 1"
sql2 = "SELECT word_2 FROM NAME"

cusor.execute(sql1)
res1 = cusor.fetchall()
print(res1)

cusor.execute(sql2)
res2 = cusor.fetchall()
for word2 in res2:
    print(word2)