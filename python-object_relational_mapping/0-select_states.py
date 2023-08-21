import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host='localhost', user=username, passwd=password, db=database, port=3306)

c = db.cursor()
c.execute("""SELECT * FROM states ORDER BY states.id ASC""")

c.fetchone()
