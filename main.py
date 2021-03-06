#Frontend
from tkinter import*
import tkinter.messagebox
import database

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Students Database Management Systems")
        self.root.geometry("1350x750")
        self.root.config(bg="cornsilk2")

        StdID = StringVar()
        Firstname= StringVar()
        Surname= StringVar()
        DOB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #function

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)
        def addData():
            if(len(StdID.get())!= 0):
                database.addStdRec(StdID.get(),Firstname.get(), Surname.get(), DOB.get(),Age.get(), Gender.get(),  Address.get() , Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(), Surname.get(), DOB.get(),Age.get(), Gender.get(),Address.get() , Mobile.get()))
        def DisplayData():
            studentlist.delete(0, END)
            for row in database.viewData():
                studentlist.insert(END,row,str(""))
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END,sd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, sd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, sd[3])
            self.txtDOB.delete(0, END)
            self.txtDOB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])
        def DeleteData():
            if (len(StdID.get()) != 0):
                database.deleteRec(sd[0])
                clearData()
                DisplayData()

        def update():
            if(len(StdID.get())!=0):
                database.deleteRec(sd[0])
                if(len(StdID.get())!=0):
                    database.addStdRec(StdID.get(),Firstname.get(), Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                    studentlist.delete(0,END)
                    studentlist.insert(database,(StdID.get(),Firstname.get(), Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))












        #Frame
        MainFrame = Frame(self.root, bg="cornsilk2")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd= 2, padx=54, pady=8, bg='cornsilk2', relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame,font=('arial', 47,'bold'),text="Student Database Management Systems",bg="cornsilk2")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70,padx=18,pady=10, bg="Ghost White" , relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300,height=400, padx=20,pady=20,relief=RIDGE,bg="cornsilk2")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1,width=1000,height=600,padx=20,relief=RIDGE, bg="Ghost White" , font=('arial', 20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE, bg="Ghost White",font=('arial', 20,'bold'),text="Student Info\n")
        DataFrameRIGHT.pack(side=RIGHT)
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID",bg="Ghost White",padx=2,pady=2)
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID , width=39)
        self.txtStdID.grid(row=0, column=1, sticky=W)

        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Firstname :", bg="Ghost White", padx=2,pady=2)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname , width=39)
        self.txtFirstname.grid(row=1, column=1, sticky=W)

        self.lblSurname = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Surname :", bg="Ghost White", padx=2,)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtSurname.grid(row=2, column=1, sticky=W)

        self.lblDOB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="DOB :", bg="Ghost White", padx=2,pady=2)
        self.lblDOB.grid(row=3, column=0, sticky=W)
        self.txtDOB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DOB, width=39)
        self.txtDOB.grid(row=3, column=1, sticky=W)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age :", bg="Ghost White", padx=2,pady=2)
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1, sticky=W)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", bg="Ghost White", padx=2,pady=2)
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1, sticky=W)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address:", bg="Ghost White", padx=2,pady=2)
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAddress.grid(row=6, column=1, sticky=W)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile:", bg="Ghost White", padx=2, pady=2)
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1, sticky=W)

        # listbox and scrollbar

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command = studentlist.yview)

        #Button

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial',20,'bold'), height=1,width=10,bd=4, command = addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command= DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command = clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command= DeleteData)
        self.btnDeleteData.grid(row=0, column=3)



        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command= update)
        self.btnUpdateData.grid(row=0, column=4)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=5)







if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
