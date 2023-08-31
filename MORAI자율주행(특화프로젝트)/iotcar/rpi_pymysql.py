
#import paho.mqtt.client as mqtt # mqtt 라이브러리 
import mysql.connector as mariadb # db연결 라이브러리

less_db = mariadb.connect(host="3.35.137.123",user='root',password='lessGO405',database='lessgo') # NALDA_db와 연결
cur = less_db.cursor() # cursor 지정

# conn = pymysql.connect(host='3.35.137.123', port=3306, user='root', passwd='lessGO405', db='sys',charset='utf8')
# cur = conn.cursor()

#cur.execute("SELECT * FROM RDi")
cur.execute("SELECT * FROM RDi WHERE id = (SELECT max(id) FROM RDi) LIMIT 1")
#print(cur.description)
# k = 0
print(cur)
# print(type(cur))
#print(dir(cur))
#print(cur.connection)
print("HI")
for row in cur:
    print(type(row))
    #print(k)
    for i in row:
        print(i)   
    #print(row[0])
    #k = k+1

# # for i in range(7):
# #     print(i)
# #     print(cur.description[i][0])
# #     print(cur.console[4])

# for row in cur.description:  
#     print(k)
#     print(row[0])
#     #print(row)
#     k = k + 1

# cur.close()
#conn.close()