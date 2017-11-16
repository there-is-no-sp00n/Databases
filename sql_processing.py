import re

#open my keys file and load the lines
my_file = open('keys.txt', 'r')
my_keys_line = my_file.readlines()

my_keys = []

#take each item/line from the txt file and make them individual items in a list
for line in my_keys_line:
	#line.strip()
	my_keys.append(line.strip())

#check to see if i actually load the items on to the program
print("my keys")
print(my_keys)

#load the relations to the program
my_rel_file = open('relation.txt', 'r')
my_rel_line = my_rel_file.readlines()


my_rel = []
fin_rel = []
#take individual items and put them in a dictionary
for line in my_rel_line:
	my_rel.append(line.strip())

for item in my_rel:
	fin_rel.append(item.split("="))
	#for item in fin_rel:
	#	for i in item:
	#		i = i.lstrip()
	
	
#print("my relations")
#print(my_rel)
print("final relations")
print(fin_rel)

eg_dict = {}
for i in range (0,len(fin_rel)):
	eg_dict[fin_rel[i][0]] = fin_rel[i][1]


#eg_dict["create table"] = "struct"
print("my dictionary")

for i in eg_dict:
	print(i, eg_dict[i])

if (eg_dict[0] == "create table"):
	print("true")

#load the sql commands for processing
my_sql_file = open('test_sql_script.txt', 'r')
my_sql_line = my_sql_file.readlines()

my_sql_commands = []

#take each item/line from the txt file and make them individual items in a list
for line in my_sql_line:
	my_sql_commands.append(line.lower().strip())

for i in range(0,len(my_sql_commands)):
	print(my_sql_commands[i])
	my_sql_commands[i] = my_sql_commands[i].split()

#check to see if i actually load the items on to the program
print(my_sql_commands)
temp = []
temp_2 = ""
for item in my_sql_commands:
	for i in item:	
		temp_2 = temp_2 + i
		print("temp_2")
		print(temp_2)
		if(temp_2 in eg_dict):
			print("in dictionary")
			temp.append(eg_dict[i])
			temp_2 = ""
		else:
			print("not in dictionary")
			temp_2 = temp_2 + " "
			print(temp_2)
	
	#elif(item in my_keys):
		#print("found one\n")
	#	continue
	#else:
		#print("sytax error\n")
	#	break

print(temp)
