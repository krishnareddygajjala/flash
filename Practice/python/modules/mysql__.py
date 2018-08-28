import MySQLdb
import yaml

with open("F:\Python WorkSpace\Parker\safecredentials.yaml") as openyaml:
    # use safe_load instead load
    safeqacredentials = yaml.safe_load(openyaml)
    safeqa = safeqacredentials['safeqa']
    safeqauser = safeqa['user']
    safeqapassword = safeqa['passwd']
    safeqahost = safeqa['host']
    safeqaport = safeqa['port']
    
#Open database connection
#db = MySQLdb.connect("localhost","root","kiran","TESTDB" )
db = MySQLdb.Connect(host = safeqahost, port = safeqaport, user=safeqauser, passwd=safeqapassword, db="sakila")

cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# disconnect from server
db.close()


##mysql -u root -P 3307 -p
##Enter password: *****
##Welcome to the MySQL monitor.  Commands end with ; or \g.
##Your MySQL connection id is 10
##Server version: 5.7.21-log MySQL Community Server (GPL)
##
##Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
##
##Oracle is a registered trademark of Oracle Corporation and/or its
##affiliates. Other names may be trademarks of their respective
##owners.
##
##Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
##
##mysql>




