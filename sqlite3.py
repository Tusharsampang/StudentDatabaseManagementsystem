import sqlite3

#backend
def End():


        def studentData():
            con= sqlite3.connect("student.db")
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, StdTD text,Firstname text, Surname text, DOB text,Age text, Gender text, Address text, Mobile text)")
            con.commit()
            con.close()

        def addStdRec( StdTD,Firstname, Surname, DOB ,Age, Gender, Address , Mobile ):
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",StdTD, Firstname, Surname, DOB ,Age, Gender, Address ,Mobile)
            con.commit()
            con.close()

        def viewData():
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows= cur.fetchall()
            con.close()
            return rows

        def deleteRec(id):
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE id=?", (id,))
            con.commit()
            con.close

        def searchData(StdID="", Firstname="",Surname="",DOB="", Age="", Gender="",Address="",Mobile=""):
            con=sqlite3.connect("Student.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student WHERE StsID=? OR Firstname=? OR Surname=? OR DOB=? OR Age=? OR Gender=? OR Address=? OR \ Mobile=?",( StdID,  Firstname, Surname,DOB,Age,Gender,Address,Mobile))
            rows=cur.fetchall()
            con.close()
            return rows

        def dataUpdate(id,StdID="",Firstname="",Surname="",DOB="",Age="",Gender='',Address="",Mobile=""):
            con=sqlite3.connect("student.db")
            cur= con.cursor()
            cur.execute("UPDATE student SET StfID=?, Firstname=?, Surname=?, DOB=?, Age=?,Gender=?,Address=?,Mobile=?,WHERE id=?","(StdId,Firstname,Surname,DOB,Age,Gender,Address,Mobile,id)")
            con.commit()
            con.close()
        studentData()