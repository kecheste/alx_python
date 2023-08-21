import MySQLdb
import sys

username = sys.argv[0]
password = sys.argv[1]
database = sys.argv[2]

db = MySQLdb.connect(
    host='localhost', user=username, passwd=password, db=database, port=3306)

c = db.cursor()
c.execute("""SELECT * FROM states""")
