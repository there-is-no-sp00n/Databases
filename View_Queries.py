import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='polo', db='USER_PRIV', autocommit=True)

cur = conn.cursor()

cur.execute ("SELECT * FROM USER_ROLE")
result = cur.fetchall()

print("Role Name		Description")
print("\n")
for row in result:
	#print("Role Name	Description")
	#for item in row:
	print (row[0].ljust(15),"\t", row[1].ljust(15))


print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

cur.execute ("SELECT * FROM USER_ACCOUNT")
result = cur.fetchall()

print("ID #	Name		Phone		My Role")
print("\n")
for row in result:
	print (row[0],"\t",row[1],"\t",row[2],"\t", row[3])

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

cur.execute ("SELECT * FROM TABLE_EX")
result = cur.fetchall()

print("Owner ID 	Table Name")
print("\n")
for row in result:
	print (row[0],"        	",row[1].ljust(15))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")

cur.execute ("SELECT * FROM PRIVILEGE")
result = cur.fetchall()

print("Priv Name 		Priv Type")
print("\n")
for row in result:
	print (row[0].ljust(15),"       ",row[1].ljust(15))

print("\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("\n")


cur.execute ("SELECT * FROM HAS_PRIV")
result = cur.fetchall()

print("Role_Name 		Priv Name")
print("\n")
for row in result:
	print (row[0].ljust(15), "        ", row[1].ljust(15))
