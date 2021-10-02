import sqlite3

#backend


def studentData():
    print("Hi")
    con= sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, StdTD text,Firstname text, Surname text, DOB text,Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addStdRec( StdID,Firstname, Surname, DOB ,Age, Gender, Address , Mobile ):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students VALUES (NULL, ?,?,?,?,?,?,?,?)",(StdID, Firstname, Surname, DOB ,Age, Gender, Address ,Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows= cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    con.commit()
    con.close


def dataUpdate(id,StdID="",Firstname="",Surname="",DOB="",Age="",Gender='',Address="",Mobile=""):
    con=sqlite3.connect("student.db")
    cur= con.cursor()
    cur.execute("UPDATE students SET StdID=?, Firstname=?, Surname=?, DOB=?, Age=?,Gender=?,Address=?,Mobile=?,WHERE id=?",\
                (StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile, id))
    con.commit()
    con.close()
try:
    studentData()
except:
    pass
