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

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.2
role = input("Enter role name: ")
desc = input("Enter role description: ")
cur.execute("INSERT INTO USER_ROLE VALUES (%s, %s)", (role, desc))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.3
cur.execute ("SELECT * FROM USER_ACCOUNT")
result = cur.fetchall()

print("ID #	Name		Phone		My Role")
print("\n")
for row in result:
	print (row[0],"\t",row[1],"\t",row[2],"\t", row[3])

owwwn = int(input("Pick an owner: "))
nam_tab = input("Enter name of table: ")
cur.execute("INSERT INTO TABLE_EX VALUES (%s, %s)", (owwwn, nam_tab))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.4
priv_name = input("Enter privilege name: ")
priv_type = ["ACCOUNT", "RELATIONAL"]
print("Enter privilege type \n Press 0 for ACCOUNT \n Press 1 for RELATIONAL")
priv_choice = int(input("What is your choice? "))

cur.execute("INSERT INTO PRIVILEGE VALUES (%s, %s)", (priv_name, priv_type[priv_choice]))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.5
#already assigning a user to a role when making the user account
#cur.execute("UPDATE INTO USER_ACCOUNT VALUES ('22', 'D.Beckham', '888-070-8888', 'coach')")

# 3.6
cur.execute ("SELECT * FROM USER_ROLE")
result = cur.fetchall()

print("Role Name		Description")
print("\n")
count = 0
for row in result:
	#print("Role Name	Description")
	#for item in row:
	print (count, row[0].ljust(15),"\t", row[1].ljust(15))
	count += 1
role_priv = int(input("Pick a role: "))
role_choi = ""
count = 0
for row in result:
	print(count)
	if count == role_priv:
		role_choi = row[0]
		break
	count += 1
print("role ",role_choi)

cur.execute ("SELECT * FROM PRIVILEGE")
result = cur.fetchall()

print("Priv Name 		Priv Type")
print("\n")
count = 0
for row in result:
	print (count, row[0].ljust(15),"       ",row[1].ljust(15))
	count += 1
priv_choi = int(input("Pick a privilege: "))
privvv = ""
count = 0
for row in result:
	if count == priv_choi:
		privvv = row[0]
		break
	count += 1
print("priv ", privvv)


cur.execute("INSERT INTO HAS_PRIV VALUES (%s, %s)", (role_choi, privvv))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.7
# when a table is created the owner is assigned, the owner has a role, and that role is assigned privileges

# 3.8
nombre_role = input("Enter role name: ")

cur.execute("SELECT * FROM HAS_PRIV WHERE roleName = %s", nombre_role)

result = cur.fetchall()

for row in result:
	print(row)

nombre_user = input("Enter user name: ")
cur.execute("SELECT name, my_role, privName FROM HAS_PRIV, USER_ACCOUNT WHERE name=%s AND my_role=roleName", nombre_user)
result = cur.fetchall()

for row in result:
	print(row)

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.8

nombre_role = input("Enter role name: ")

cur.execute("SELECT * FROM HAS_PRIV WHERE roleName = %s", nombre_role)

result = cur.fetchall()

for row in result:
	print(row)

nombre_user = input("Enter user name: ")
cur.execute("SELECT name, my_role, privName FROM HAS_PRIV, USER_ACCOUNT WHERE name=%s AND my_role=roleName", nombre_user)
result = cur.fetchall()

for row in result:
	print(row)

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

# 3.9
cur.execute ("SELECT * FROM USER_ROLE")
result = cur.fetchall()

print("Role Name		Description")
print("\n")
for row in result:
	#print("Role Name	Description")
	#for item in row:
	print (row[0].ljust(15),"\t", row[1].ljust(15))

nombre_role = input("Enter role name to revoke privileges: ")

cur.execute("SELECT * FROM HAS_PRIV WHERE roleName = %s", nombre_role)

result = cur.fetchall()

for row in result:
	print(row)

del_priv = input("Enter priv to revoke: ")
cur.execute("DELETE FROM HAS_PRIV WHERE privName = %s", del_priv)






