import MySQLdb

# Open database connection
#db = MySQLdb.connect("localhost","root","kiran","TESTDB" )
db = MySQLdb.Connect(host='LAPTOP-8SDH3R8D', port=3307, user="root1", passwd="kiran", db="krishna")

cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
#data1 = cursor.fetchall()
print "Database version : %s " % data

# disconnect from server
db.close()