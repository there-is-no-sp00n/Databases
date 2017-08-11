import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='polo', db='USER_PRIV', autocommit=True)

cur = conn.cursor()

input_arr = []

# 3.1
name = input("Enter name of the User Account: ")
cell = input("Enter number of the User Account: ")
cur.execute ("SELECT * FROM USER_ACCOUNT")
total_num = cur.rowcount + 1
#print(total_num)
cur.execute ("SELECT * FROM USER_ROLE")
result = cur.fetchall()

count = 0
print("\n")
print("#	Role Name		Description")
for row in result:
	print (count, "\t", row[0].ljust(15),"\t", row[1].ljust(15))
	count += 1

count = 0
choice = int(input("Enter number of the role: "))
#choice -= 1
role = ""
	
for row in result:
	if (count == choice):
		role = row[0]
	count += 1
print(role)
cur.execute("INSERT INTO USER_ACCOUNT VALUES (%s, %s, %s, %s)", (total_num, name, cell, role))

# 3.2
#cur.execute("INSERT INTO USER_ROLE VALUES ('coach', 'los deportes')")

# 3.3
#cur.execute("INSERT INTO TABLE_EX VALUES ('10', 'Table_11')")

# 3.4
#cur.execute("INSERT INTO PRIVILEGE VALUES ('REFERENCES', 'ACCOUNT')")

# 3.5
#cur.execute("INSERT INTO USER_ACCOUNT VALUES ('22', 'D.Beckham', '888-070-8888', 'coach')")

# 3.6
#cur.execute("INSERT INTO HAS_PRIV VALUES ('admin', 'REFERENCES')")

# 3.7
