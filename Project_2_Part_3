import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='polo', db='USER_PRIV', autocommit=True)

cur = conn.cursor()

# INSERT for USER_ROLE
cur.execute("INSERT INTO USER_ROLE VALUES ('admin', 'admin_power')")
cur.execute("INSERT INTO USER_ROLE VALUES ('advisor', 'pick classes')")
cur.execute("INSERT INTO USER_ROLE VALUES ('president', 'all the power')")
cur.execute("INSERT INTO USER_ROLE VALUES ('student', 'no power at all')")
cur.execute("INSERT INTO USER_ROLE VALUES ('professor', 'knowledge power')")

# INSERT for USER_ACCOUNTS
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('1', 'J.Fitz', '888-888-8888', 'admin')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('2', 'J.Neymar', '111-888-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('3', 'L.Messi', '111-238-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('4', 'L.Suarez', '231-888-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('5', 'C.Ronaldo', '134-888-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('6', 'K.Benzema', '111-438-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('7', 'G.Bale', '111-843-8888', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('8', 'E.Hazard', '111-888-8458', 'advisor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('9', 'J.Mourinho', '111-338-8888', 'president')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('10', 'N.Matic', '111-888-0088', 'professor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('11', 'P.Coutinho', '111-238-8588', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('12', 'A.Wenger', '777-888-8888', 'professor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('13', 'A.Conte', '111-448-8998', 'professor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('14', 'D.Costa', '333-888-8568', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('15', 'R.Abrahamovic', '111-348-8094', 'advisor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('16', 'F.Perez', '001-388-8888', 'advisor')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('17', 'P.Pogba', '111-058-8540', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('18', 'Z.Ibrahimovic', '511-878-8328', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('19', 'K.Mbappe', '021-833-8853', 'student')")
cur.execute("INSERT INTO USER_ACCOUNT VALUES ('20', 'F.Torres', '105-807-8302', 'student')")

# INSERT for TABLE_EX
cur.execute("INSERT INTO TABLE_EX VALUES ('2', 'Table_1')")
cur.execute("INSERT INTO TABLE_EX VALUES ('5', 'Table_2')")
cur.execute("INSERT INTO TABLE_EX VALUES ('17', 'Table_3')")
cur.execute("INSERT INTO TABLE_EX VALUES ('18', 'Table_4')")
cur.execute("INSERT INTO TABLE_EX VALUES ('8', 'Table_5')")
cur.execute("INSERT INTO TABLE_EX VALUES ('9', 'Table_6')")
cur.execute("INSERT INTO TABLE_EX VALUES ('19', 'Table_7')")
cur.execute("INSERT INTO TABLE_EX VALUES ('20', 'Table_8')")
cur.execute("INSERT INTO TABLE_EX VALUES ('7', 'Table_9')")
cur.execute("INSERT INTO TABLE_EX VALUES ('10', 'Table_10')")

# INSERT for PRIVILEGE (ACCOUNT)
cur.execute("INSERT INTO PRIVILEGE VALUES ('SELECT', 'ACCOUNT')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('CREATE_TABLE', 'ACCOUNT')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('CREATE_VIEW', 'ACCOUNT')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('ALTER', 'ACCOUNT')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('DROP', 'ACCOUNT')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('MODIFY', 'ACCOUNT')")

# INSERT for PRIVILEGE (RELATIONAL)
cur.execute("INSERT INTO PRIVILEGE VALUES ('INSERT', 'RELATIONAL')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('DELETE', 'RELATIONAL')")
cur.execute("INSERT INTO PRIVILEGE VALUES ('UPDATE', 'RELATIONAL')")

# INSERT for HAS_PRIV
cur.execute("INSERT INTO HAS_PRIV VALUES ('admin', 'SELECT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('admin', 'CREATE_TABLE')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('admin', 'ALTER')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('admin', 'DROP')")

cur.execute("INSERT INTO HAS_PRIV VALUES ('president', 'SELECT')")

cur.execute("INSERT INTO HAS_PRIV VALUES ('student', 'INSERT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('student', 'DELETE')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('student', 'UPDATE')")

cur.execute("INSERT INTO HAS_PRIV VALUES ('professor', 'INSERT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('professor', 'SELECT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('professor', 'ALTER')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('professor', 'MODIFY')")

cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'INSERT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'SELECT')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'ALTER')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'MODIFY')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'DROP')")
cur.execute("INSERT INTO HAS_PRIV VALUES ('advisor', 'DELETE')")
