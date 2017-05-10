#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb

string = "i211s17_euhde" 			#change this to yours
password = "my+sql=i211s17_euhde"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """
<html>
    <body>
        <h1> Faculty Member Deleted </h1>
        <p><a href="FacultyView.cgi">Go Back</a></p>
    </body>
</html>"""

try:
    form = cgi.FieldStorage()
    fid = form.getfirst("fid", "0")
    SQL = "DELETE FROM Faculty WHERE FacultyID = " + fid + ";"
    cursor.execute(SQL)
    db_con.commit()
except Exception as e:		#Here we handle the error
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "\nError:", e)
