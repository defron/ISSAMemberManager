import sqlite3
import sys

class Database(object):
    '''Class to handle connection to sqlite3 database'''
    def __init__(self, db_file = 'memberdb.sqlite3'):
        self.con = sqlite3.connect(db_file)

        '''
	def insert(self, id,fname, lname, email, phone, gradyear):
		cur = self.con.cursor()
		cur.execute("INSERT INTO people VALUES (:id, :fname,:lname,:email,:phone,:gradyear)", {"id":id, "fname":fname,
		                                            "lname":lname, "email":email, "phone":phone, "gradyear":gradyear})
		rows = cur.fetchall()
		self.con.commit()

		return "Success!"
	'''

    def insert(self, fname, lname, email, phone, gradyear):
        cur = self.con.cursor()

        #Create a list of all the values to be inserted in the table
        values = (fname, lname, email, phone, gradyear)

        #Create the sql query
        query = "INSERT INTO people(firstname, lastname, email, phone, gradyear) VALUES (?,?,?,?,?)"

        #Execute the query, using the above list of values.
        cur.execute(query, values)

        self.con.commit()
        return "Success!"

    '''
	def update(self, id, column, new_value):
		cur = self.con.cursor()

		cur.execute("Update people SET %s=\'%s\' WHERE id=%d" %(column, new_value, id))

		self.con.commit()
		return "Success!"
    '''

    def update(self, id,table, **new_values):
        cur = self.con.cursor()
        if(table == "BoardMember"):
            cur.execute("Update BoardMember set titleid=:titleid, boardyear=:year WHERE id=:id",
                        {"id": id, "titleid": new_values.get("titleid"), "year": new_values.get("year")})
        elif(table == "People"):
            cur.execute("Update People set firstname=:fname, lastname=:lname, email=:email, phone=:phone, gradyear=:year WHERE id=:id",
                        {"id": id, "fname": new_values.get("fname"), "lname": new_values.get("lname"),
                         "email": new_values.get("email"), "phone": new_values.get("phone"),
                         "year": new_values.get("year")})
        for key, value in iter(new_values.items()):
            cur.execute("Update %s SET %s=\'%s\' WHERE id=%d" %(table, key, value, id))

        self.con.commit()
        return "Success!"

    def delete(self, id):
        cur = self.con.cursor()

        cur.execute("DELETE FROM people WHERE id=:id", {"id":id}  )

        self.con.commit()
        return "Success!"


    def print(self):
        cur = self.con.cursor()

        cur.execute("SELECT * FROM people;")

        rows = cur.fetchall()

        for row in rows:
            print (row)
        return "Success!"







































'''
if __name__ == '__main__':
db = database()
sql = "SELECT * from PEOPLE"
records = db.select(sql)
for record in records:
	print (record)
==================================================================
con = sqlite3.connect('memberdb.sqlite3')

cur = con.cursor()

cur.execute("INSERT INTO People VALUES (6,'Vu', 'Cao', 'cdhvu@yahoo.com', '012663116', 2016);")

cur.execute("SELECT * FROM People")
rows = cur.fetchall()

for row in rows:
print (row)

con.commit()
===================================================================
class database:
    import sqlite3

database.open()
	    conn = sqlite3.connect('memberdb.db')
        c = conn.cursor()

database.runsql()
def dataentry():
c.execute("INSERT INTO PEOPLE (ID, FirstName, LastName, Email, Phone, GradYear) VALUES (?,?,?,?,?,?), source")
conn.commit()
# for source, i'm not sure what to put here. I'll do more research over the week.

database.close()
    conn.close()
'''
