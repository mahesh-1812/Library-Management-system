from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import mysql.connector

class librarySystem:

    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1280x900")
        self.root.maxsize(1280,900)


        self.member_var=StringVar()
        self.Firstname_var=StringVar()
        self.Lastname_var=StringVar()
        self.IDnumber_var=StringVar()
        self.Contact_var=StringVar()
        self.addressline1_var=StringVar()
        self.addressline2_var=StringVar()
        self.class_var=StringVar()
        self.year_var=StringVar()
        self.bookName_var=StringVar()
        self.author_var=StringVar()
        self.duedate_var=StringVar()
        self.returndate_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.bookprice_var=StringVar()
        self.copies_var=StringVar()
        self.latefine_var=StringVar()
        self.bookid_var=StringVar()



        headerlabel=Label(root,text="Library Management System",bg="powder blue",fg="black",font=("Times New Roman",30,"bold"),bd=12,relief=SUNKEN)
        headerlabel.pack(side=TOP,fill=X)

        #==========================================================Frame============================================================================================

        frame=Frame(root,bg="powder blue",bd=12,relief=SUNKEN)
        frame.place(x=0,y=100,width=1280,height=400)

        #========================================================Leftdata frame================================================================

        framedetailsleft=LabelFrame(frame,text="Member details",bg="powder blue",fg="green",bd=6,relief=RIDGE,font=("Times New Roman",12,"bold"))
        framedetailsleft.place(x=0,y=5,height=350,width=750)

        lblmember=Label(framedetailsleft,text="Member type",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(framedetailsleft,font=("Times New Roman",12),textvariable=self.member_var,state="readonly")
        comMember["value"]=("Select","Admin Staff","Student","Guest")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblfname=Label(framedetailsleft,text="First Name",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblfname.grid(row=1,column=0)
        lblfname_entry=Entry(framedetailsleft,textvariable=self.Firstname_var,width=30)
        lblfname_entry.grid(row=1,column=1,sticky=W)

        lbllname=Label(framedetailsleft,text="Last Name",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lbllname.grid(row=2,column=0)
        lbllname_entry=Entry(framedetailsleft,textvariable=self.Lastname_var,width=30)
        lbllname_entry.grid(row=2,column=1,sticky=W)

        lblID_number=Label(framedetailsleft,text="ID number",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblID_number.grid(row=3,column=0)
        lblID_number_entry=Entry(framedetailsleft,textvariable=self.IDnumber_var,width=30)
        lblID_number_entry.grid(row=3,column=1,sticky=W)

        lblcontact=Label(framedetailsleft,text="Contact",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblcontact.grid(row=4,column=0)
        lblcontact_entry=Entry(framedetailsleft,textvariable=self.Contact_var,width=30)
        lblcontact_entry.grid(row=4,column=1,sticky=W)

        lbladdress1=Label(framedetailsleft,text="AddressLine1",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lbladdress1.grid(row=5,column=0)
        lblAddres1_entry=Entry(framedetailsleft,textvariable=self.addressline1_var,width=30)
        lblAddres1_entry.grid(row=5,column=1,sticky=W)

        lbladdress2=Label(framedetailsleft,text="AddressLine2",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lbladdress2.grid(row=6,column=0)
        lblAddres2_entry=Entry(framedetailsleft,textvariable= self.addressline2_var,width=30)
        lblAddres2_entry.grid(row=6,column=1,sticky=W)

        lblclass=Label(framedetailsleft,text="Class",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblclass.grid(row=7,column=0)
        lblclass_entry=Entry(framedetailsleft,textvariable=self.class_var,width=30)
        lblclass_entry.grid(row=7,column=1)

        lblyear=Label(framedetailsleft,text="Year",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblyear.grid(row=8,column=0)
        Lblyear_entry=Entry(framedetailsleft,textvariable=self.year_var,width=30)
        Lblyear_entry.grid(row=8,column=1)

        lblbkname=Label(framedetailsleft,text="Book Name",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblbkname.grid(row=0,column=2)
        lblbkname_entry=Entry(framedetailsleft,textvariable=self.bookName_var,width=30)
        lblbkname_entry.grid(row=0,column=3)

        lblauthor=Label(framedetailsleft,text="Author",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblauthor.grid(row=1,column=2)
        lblauthor_entry=Entry(framedetailsleft,textvariable=self.author_var,width=30)
        lblauthor_entry.grid(row=1,column=3)

        lblduedate=Label(framedetailsleft,text="Due Date",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblduedate.grid(row=2,column=2)
        lblduedate_entry=Entry(framedetailsleft,textvariable=self.duedate_var,width=30)
        lblduedate_entry.grid(row=2,column=3)

        Lblreturn_date=Label(framedetailsleft,text="Return Date",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        Lblreturn_date.grid(row=3,column=2)
        Lblreturn_date_entry=Entry(framedetailsleft,textvariable=self.returndate_var,width=30)
        Lblreturn_date_entry.grid(row=3,column=3)

        lbl_latefee=Label(framedetailsleft,text="Date Overdue",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_latefee.grid(row=4,column=2)
        lbl_latefee_entry=Entry(framedetailsleft,textvariable=self.dateoverdue_var,width=30)
        lbl_latefee_entry.grid(row=4,column=3)

        lblbook_prce=Label(framedetailsleft,text="Book Price",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblbook_prce.grid(row=5,column=2)
        lblbook_prce_entry=Entry(framedetailsleft,textvariable=self.bookprice_var,width=30)
        lblbook_prce_entry.grid(row=5,column=3)

        lblcopies=Label(framedetailsleft,text="Copies",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblcopies.grid(row=6,column=2)
        lblcopies_entry=Entry(framedetailsleft,textvariable=self.copies_var,width=30)
        lblcopies_entry.grid(row=6,column=3)

        lbl_latefine=Label(framedetailsleft,text="Late Fine",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_latefine.grid(row=7,column=2)
        lbl_latefine_entry=Entry(framedetailsleft,textvariable=self.latefine_var,width=30)
        lbl_latefine_entry.grid(row=7,column=3)

        lblbookid=Label(framedetailsleft,text="Book ID",font=("Times New Roman",12,"bold"),bg="powder blue",padx=2,pady=6)
        lblbookid.grid(row=8,column=2)
        lblbookid_entry=Entry(framedetailsleft,textvariable=self.bookid_var,width=30)
        lblbookid_entry.grid(row=8,column=3)

        #================================================Rightdata frame=============================================================

        framedetailsright=LabelFrame(frame,text="Book details",bg="powder blue",fg="green",bd=6,relief=RIDGE,font=("Times New Roman",12,"bold"))
        framedetailsright.place(x=590,y=5,width=650,height=350)


        listscrollbar=Scrollbar(framedetailsright)
        listscrollbar.grid(row=0,column=1,sticky=NS)        
        self.txtbox=Text(framedetailsright,font=("Times New Roman",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        LstBook=["People We meet on Vacation","5 AM club","Rich Dad Poor Dad","Think and grow rich","Python for Data Science","Into Python"
        "RUle of Wolves","The Push","Data Structure","Into Machine Learning","One Last Stop","Last One to Die","Good Sister","The Broken",
        "The Boy I am","Forest Of vanishing stars","Texas 1934","Two friends","Loop","Ghost in threat","Vampire Diaries","Peaces",
        "The shimmering state","SorrowLand","Python for everybody"]

        def selectbook(self,event=" "):
            value=str(listbox.get(listbox.curselection))
            x=value
            if (x=="People We meet on Vacation"):
                self.bookName_var.set("Rich Dad Poor Dad")
                self.author_var.set("Paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.duedate_var.set(d1)
                self.returndate_var.set(d3)
                self.dateoverdue_var.set("NO")
                self.bookprice_var.set("Rs.690")
                self.copies_var.set("2")
                self.latefine_var.set("Rs.50")
                self.bookid_var.set("BK450718")

        listbox=Listbox(framedetailsright,font=("Times New Roman",12,"bold"),width=35,height=16)
        listbox.bind("<<ListboxSelect>>",selectbook)
        listbox.grid(row=0,column=0)
        listscrollbar.config(command=listbox.yview)

        for item in LstBook:
            listbox.insert(END,item)


        #===================================================Button Frame=================================================================
        btnframe=Frame(root,bg="powder blue",bd=10,relief=SUNKEN)
        btnframe.place(x=0,y=515,width=1280,height=65)

        btnAdd_data=Button(btnframe,command=self.add_data,text="ADD DATA",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btnAdd_data.grid(row=0,column=0)

        btnupdate_data=Button(btnframe,command=self.update_data,text="Update ",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btnupdate_data.grid(row=0,column=1)

        btnshow_data=Button(btnframe,command=self.show_data,text="Show Data",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btnshow_data.grid(row=0,column=2)

        btndelete_data=Button(btnframe,command=self.delete_dta,text="Delete",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btndelete_data.grid(row=0,column=3)

        btnreset_data=Button(btnframe,command=self.reset,text="Reset ",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btnreset_data.grid(row=0,column=4)

        btnexit=Button(btnframe,command=self.iexit,text="Exit",font=("Arial" ,12,"bold"),bg="white",fg="black",width=20)
        btnexit.grid(row=0,column=5)
        #=================================================database frame==================================================================
        framedetails=Frame(root,bg="powder blue",bd=12,relief=SUNKEN,padx=20)
        framedetails.place(x=0,y=590,width=1280,height=200)

        table_frame=Frame(framedetails,bg="powder blue",bd=6,relief=RAISED)
        table_frame.place(x=0,y=2,width=1280,height=200)

        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,column=("membertype","Firstname","Lastname","IDNumber","Contact","addressline1","addressline2","class","year","bookName","author","duedate","returndate","dateoverdue","bookprice","copies","latefine","bookid"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("Firstname",text="First Name")
        self.library_table.heading("Lastname",text="Last Name")
        self.library_table.heading("IDNumber",text="ID Number")
        self.library_table.heading("Contact",text="Mobile Number")
        self.library_table.heading("addressline1",text="Address 1")
        self.library_table.heading("addressline2",text="Address 2")
        self.library_table.heading("class",text="Class")
        self.library_table.heading("year",text="Year")
        self.library_table.heading("bookName",text="Book Name")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("returndate",text="Return Date")
        self.library_table.heading("dateoverdue",text="Date Overdue")
        self.library_table.heading("bookprice",text="Book Price")
        self.library_table.heading("copies",text="Copies")
        self.library_table.heading("latefine",text="Late Fine")
        self.library_table.heading("bookid",text="Book ID")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("Firstname",width=100)
        self.library_table.column("Lastname",width=100)
        self.library_table.column("IDNumber",width=100)
        self.library_table.column("Contact",width=100)
        self.library_table.column("addressline1",width=100)
        self.library_table.column("addressline2",width=100)
        self.library_table.column("class",width=100)
        self.library_table.column("year",width=100)
        self.library_table.column("bookName",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("returndate",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("bookprice",width=100)
        self.library_table.column("copies",width=100)
        self.library_table.column("latefine",width=100)
        self.library_table.column("bookid",width=100)


        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="127.0.0.1", username="root",password="M@hesh7045",database="librarydb")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO new_table1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),
                                                                                                                self.Firstname_var.get(),
                                                                                                                self.Lastname_var.get(),
                                                                                                                self.IDnumber_var.get(),
                                                                                                                self.Contact_var.get(),
                                                                                                                self.addressline1_var.get(),
                                                                                                                self.addressline2_var.get(),
                                                                                                                self.class_var.get(),
                                                                                                                self.year_var.get(),
                                                                                                                self.bookName_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.returndate_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.bookprice_var.get(),
                                                                                                                self.copies_var.get(),
                                                                                                                self.latefine_var.get(),
                                                                                                                self.bookid_var.get()))
        # my_cursor.execute("SELECT * FROM new_table")
        # data=my_cursor.fetchall()
        # print(data)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success !!")

    def update_data(self):
        conn=mysql.connector.connect(host="127.0.0.1", username="root",password="M@hesh7045",database="librarydb")
        my_cursor=conn.cursor()
        my_cursor.execute(" UPDATE new_table1 set Member Type=%s,First Name=%s,Last Name=%s,Contact=%s, Addressline1=%s, Addressline2=%s, class=%s, year=%s, Bookname=%s, Author=%s, Duedate=%s, Returndate=%s, Dateoverdue=%s, Bookprice=%s, Copies=%s, Latefine=%s, Bookid=%s where ID number=%s)",
                                                                                                                (self.member_var.get(),
                                                                                                                self.Firstname_var.get(),
                                                                                                                self.Lastname_var.get(),
                                                                                                                self.Contact_var.get(),
                                                                                                                self.addressline1_var.get(),
                                                                                                                self.addressline2_var.get(),
                                                                                                                self.class_var.get(),
                                                                                                                self.year_var.get(),
                                                                                                                self.bookName_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.duedate_var.get(),
                                                                                                                self.returndate_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.bookprice_var.get(),
                                                                                                                self.copies_var.get(),
                                                                                                                self.latefine_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.IDnumber_var.get()))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Updated Successfully !!")


    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1", username="root",password="M@hesh7045",database="librarydb")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM new_table1")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.Firstname_var.set(row[1]),
        self.Lastname_var.set(row[2]),
        self.IDnumber_var.set(row[3]),
        self.Contact_var.set(row[4]),
        self.addressline1_var.set(row[5]),
        self.addressline2_var.set(row[6]),
        self.class_var.set(row[7]),
        self.year_var.set(row[8]),
        self.bookName_var.set(row[9]),
        self.author_var.set(row[10]),
        self.duedate_var.set(row[11]),
        self.returndate_var.set(row[12]),
        self.dateoverdue_var.set(row[13]),
        self.bookprice_var.set(row[14]),
        self.copies_var.set(row[15]),
        self.latefine_var.set(row[16]),
        self.bookid_var.set(row[17]),

    def show_data(self):
        self.txtbox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtbox.insert(END,"First Name\t\t"+self.Firstname_var.get()+"\n")
        self.txtbox.insert(END,"Last Name\t\t"+self.Lastname_var.get()+"\n")
        self.txtbox.insert(END,"ID Number\t\t"+self.IDnumber_var.get()+"\n")
        self.txtbox.insert(END,"Contact\t\t"+self.Contact_var.get()+"\n")
        self.txtbox.insert(END,"Address1\t\t"+self.addressline1_var.get()+"\n")
        self.txtbox.insert(END,"Address2\t\t"+self.addressline2_var.get()+"\n")
        self.txtbox.insert(END,"Class\t\t"+self.class_var.get()+"\n")
        self.txtbox.insert(END,"Year\t\t"+self.year_var.get()+"\n")
        self.txtbox.insert(END,"Book Name\t\t"+self.bookName_var.get()+"\n")
        self.txtbox.insert(END,"Author\t\t"+self.author_var.get()+"\n")
        self.txtbox.insert(END,"Duedate\t\t"+self.duedate_var.get()+"\n")
        self.txtbox.insert(END,"Returndate\t\t"+self.returndate_var.get()+"\n")
        self.txtbox.insert(END,"Dateoverdue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtbox.insert(END,"Bookprice\t\t"+self.bookprice_var.get()+"\n")
        self.txtbox.insert(END,"Copies\t\t"+self.copies_var.get())+"\n"
        self.txtbox.insert(END,"Latefine\t\t"+self.latefine_var.get()+"\n")
        self.txtbox.insert(END,"Bookid\t\t"+self.bookid_var.get()+"\n")

    def reset(self):
        self.member_var.set("")
        self.Firstname_var.set(""),
        self.Lastname_var.set(""),
        self.IDnumber_var.set(""),
        self.Contact_var.set(""),
        self.addressline1_var.set(""),
        self.addressline2_var.set(""),
        self.class_var.set(""),
        self.year_var.set(""),
        self.bookName_var.set(""),
        self.author_var.set(""),
        self.duedate_var.set(""),
        self.returndate_var.set(""),
        self.dateoverdue_var.set(""),
        self.bookprice_var.set(""),
        self.copies_var.set(""),
        self.latefine_var.set(""),
        self.bookid_var.set(""),
        self.txtbox.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("Library system","Do you want to exit")
        if iexit>0:
            root.destroy()
        else:
            return

    def delete_dta(self):
        if self.IDnumber_var=="" or self.bookid_var=="":
            messagebox.showinfo("Error ! Select one user")
        else:
            conn=mysql.connector.connect(host="127.0.0.1", username="root",password="M@hesh7045",database="librarydb")
            my_cursor=conn.cursor()
            my_cursor.execute("DELETE FROM new_table1 where ID number=%s",self.IDnumber_var.get())
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Deleted Successfully")

if __name__ =="__main__":
    root=Tk()
    obj=librarySystem(root)
    root.mainloop()
