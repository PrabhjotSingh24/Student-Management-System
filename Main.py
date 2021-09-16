# Developed by Prabhjot Singh

# Completion date-24/11/2020
# Completion time-09:01PM


# Student Management System

# Importing required modules
import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
from pickle import load

# Additional Variables
heading_font_size = 17  # <-- change these values to get outputs smaller or bigger
output_font_size = 15  # <-- change these values to get outputs smaller or bigger
green_shade = "#34822a"
master_key = True  # <-- Change this to True to bypass authentication

# SQL Connection with Python
try:
    mydb = sql.connect(
        host="localhost", user="root", passwd="", database="students_records"
    )
    curs = mydb.cursor()
except:
    print("An Error Occurred! in connectivity block")
    raise

# Command Functions


def show_databases():
    import mysql.connector as mycon

    w3 = Toplevel()
    w3.resizable(0, 0)
    w3.title("Output")
    w3.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 450
    wh = 350
    w3.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    w3.config(bg="white")
    mydb = mycon.connect(host="localhost", user="root", passwd="")
    curs = mydb.cursor()
    curs.execute("Show databases")
    simple_label = Label(
        w3,
        text="< Databases >",
        fg=green_shade,
        bg="white",
        font=("COCOGOOSE", heading_font_size),
    )
    simple_label.pack()
    for databases in curs:
        sdlabel = Label(
            w3,
            text=databases,
            anchor=CENTER,
            fg=green_shade,
            bg="white",
            font=("calibre", output_font_size),
        )
        sdlabel.pack()


def show_tables():
    w4 = Toplevel()
    w4.resizable(0, 0)
    w4.title("Output")
    w4.iconbitmap("./IcoImages/pslogo.ico")
    w4.config(bg="white")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 250
    wh = 200
    w4.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")

    try:
        curs.execute("show tables")
        Label(
            w4,
            text="< Tables >",
            anchor=CENTER,
            fg=green_shade,
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).pack()
        for tab in curs:
            stlabel = Label(
                w4,
                text=tab,
                anchor=CENTER,
                fg=green_shade,
                bg="white",
                font=("calibre", output_font_size),
            )
            stlabel.pack()
    except:
        print("an error occurred in show_tables block")
        raise


def create_table():
    w5 = Toplevel()
    w5.resizable(0, 0)
    w5.title("Input")
    w5.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 200
    wh = 100
    w5.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    try:
        tname = StringVar()
        Label(w5, text="Table Name:").grid(row=0, column=0)
        tablename = Entry(w5, textvariable=tname)
        tablename.grid(row=0, column=1)

        def execution():
            curs.execute(
                "create table "
                + str(tname.get())
                + "(rollno int primary key ,name varchar(50) not null,classs varchar(3),stream varchar(20) default 'xxxx',section varchar(2),total int default 0)"
            )

            messagebox.showinfo("Output", "Table Created Successfully")
            mydb.commit()
            w5.destroy()

        Button(
            w5,
            text="Submit",
            font=("COCOGOOSE", 10),
            bg=green_shade,
            fg="white",
            command=execution,
            borderwidth=0,
            border=0,
        ).place(x=70, y=40)
    except:
        print("an error occurred in create_table block")
        mydb.rollback()


def display_Struc():
    w6 = Toplevel()
    w6.resizable(0, 0)
    w6.title("Input")
    w6.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 200
    wh = 100
    w6.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")

    tname = StringVar()
    Label(w6, text="Table Name:").grid(row=0, column=0)
    tablename = Entry(w6, textvariable=tname)
    tablename.grid(row=0, column=1)

    def misc():
        curs.execute("desc %s" % tname.get())
        w11 = Toplevel()
        w11.resizable(0, 0)
        w11.title("Output")
        w11.config(bg="white")
        w11.iconbitmap("./IcoImages/pslogo.ico")
        Label(
            w11,
            text="Field",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=0)
        Label(
            w11,
            text="Type",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=1)
        Label(
            w11,
            text="Null",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=2)
        Label(
            w11,
            text="Key",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=3)
        Label(
            w11,
            text="Default",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=4)
        Label(
            w11,
            text="Extra",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=5)
        for i, records in enumerate(curs):
            Label(
                w11,
                text=records[0],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=0)
            Label(
                w11,
                text=records[1],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=1)
            Label(
                w11,
                text=records[2],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=2)
            Label(
                w11,
                text=records[3],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=3)
            Label(
                w11,
                text=records[4],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=4)
            Label(
                w11,
                text=records[5],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=5)

    Button(
        w6,
        text="Submit",
        font=("COCOGOOSE", 10),
        bg=green_shade,
        fg="white",
        command=misc,
        borderwidth=0,
        border=0,
    ).place(x=70, y=35)

    for i in curs:
        print(i)


def add_rec():
    w7 = Toplevel()
    w7.resizable(0, 0)
    w7.title("Input")
    w7.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 200
    wh = 210
    w7.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    try:
        tname = StringVar()
        rno_var = StringVar()
        naam_var = StringVar()
        clas_var = StringVar()
        strem_var = StringVar()
        sec_var = StringVar()
        total_var = StringVar()
        Label(w7, text="Table Name").grid(row=0, column=0)
        Label(w7, text="RollNo").grid(row=1, column=0)
        Label(w7, text="Name").grid(row=2, column=0)
        Label(w7, text="Class").grid(row=3, column=0)
        Label(w7, text="Stream").grid(row=4, column=0)
        Label(w7, text="Section").grid(row=5, column=0)
        Label(w7, text="Total Marks").grid(row=6, column=0)

        e1 = Entry(w7, textvariable=tname)
        e1.grid(row=0, column=1)
        e2 = Entry(w7, textvariable=rno_var)
        e2.grid(row=1, column=1)
        e3 = Entry(w7, textvariable=naam_var)
        e3.grid(row=2, column=1)
        e3.insert(0, "''")
        e4 = Entry(w7, textvariable=clas_var)
        e4.grid(row=3, column=1)
        e5 = Entry(w7, textvariable=strem_var)
        e5.grid(row=4, column=1)
        e5.insert(0, "''")
        e6 = Entry(w7, textvariable=sec_var)
        e6.grid(row=5, column=1)
        e6.insert(0, "''")
        e7 = Entry(w7, textvariable=total_var)
        e7.grid(row=6, column=1)

        def executee():
            rno = rno_var.get()
            naam = naam_var.get()
            clas = clas_var.get()
            strem = strem_var.get()
            sec = sec_var.get()
            total = total_var.get()
            query = "INSERT INTO %s(rollno,name,classs,stream,section,total) values(%i,%s,%i,%s,%s,%i)" % (
                tname.get(),
                int(rno),
                f"{naam}",
                int(clas),
                f"{strem}",
                f"{sec}",
                int(total),
            )
            curs.execute(query)
            mydb.commit()
            messagebox.showinfo("Output", "Record Added Successfully")
            rno_var.set("")
            naam_var.set("")
            clas_var.set("")
            strem_var.set("")
            sec_var.set("")
            total_var.set("")

        Button(
            w7,
            text="Submit",
            font=("COCOGOOSE", 10),
            border=0,
            borderwidth=0,
            fg="white",
            bg=green_shade,
            command=executee,
        ).place(x=67, y=165)

    except:
        mydb.rollback()
        print("An Error Occurred in add_rec block")
        raise


def update_rec():
    w8 = Toplevel()
    w8.resizable(0, 0)
    w8.title("Input")
    w8.iconbitmap("./IcoImages/pslogo.ico")
    w8.config(bg="white")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 250
    wh = 150
    w8.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    try:
        tname = StringVar()
        clas = StringVar()
        total = StringVar()
        roll = StringVar()
        tname_label = Label(w8, text="Table Name:", bg="white")
        tname_label.grid(row=0, column=0)
        clas_label = Label(w8, text="Class:", bg="white")
        clas_label.grid(row=1, column=0)
        tname_entry = Entry(w8, textvariable=tname, width=30)
        tname_entry.grid(row=0, column=1)
        clas_entry = Entry(w8, textvariable=clas, width=30)
        clas_entry.grid(row=1, column=1)
        total_label = Label(w8, text="Total:", bg="white")
        total_label.grid(row=2, column=0)
        tname_entry = Entry(w8, textvariable=total, width=30)
        tname_entry.grid(row=2, column=1)
        roll_label = Label(w8, text="RollNo:", bg="white")
        roll_label.grid(row=3, column=0)
        roll_entry = Entry(w8, textvariable=roll, width=30)
        roll_entry.grid(row=3, column=1)

        def execute():
            if total.get() == "":
                curs.execute(
                    "update %s set classs=%i where rollno = %s"
                    % (tname.get(), int(clas.get()), int(roll))
                )
                messagebox.showinfo("Output", "Record Updated Successfully")
                mydb.commit()
            elif clas.get() == "":
                curs.execute(
                    "update %s set total=%i where rollno = %i"
                    % (tname.get(), int(total.get()), int(roll))
                )
                messagebox.showinfo("Output", "Record Updated Successfully")
                mydb.commit()
            else:
                curs.execute(
                    "update %s set total=%i,classs=%i where rollno=%i"
                    % (tname.get(), int(total.get()), int(clas.get()), int(roll.get()))
                )
                messagebox.showinfo("Output", "Record Updated Successfully")
                mydb.commit()
            clas.set("")
            total.set("")
            roll.set("")

        submit_button = Button(
            w8,
            text="SUBMIT",
            font=("COCOGOOSE", 10),
            command=execute,
            borderwidth=0,
            fg="white",
            bg="#34822a",
        )
        submit_button.place(x=95, y=100)
    except:
        mydb.rollback()
        print("An error occured in update_rec block")


def fetch_data():
    w9 = Toplevel()
    w9.resizable(0, 0)
    w9.title("Input")
    w9.iconbitmap("./IcoImages/pslogo.ico")
    w9.config(bg="white")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 250
    wh = 120
    w9.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    tname = StringVar()
    tname_label = Label(w9, text="Table Name:", bg="white")
    tname_label.grid(row=0, column=0)
    tname_entry = Entry(w9, textvariable=tname, width=30)
    tname_entry.grid(row=0, column=1)
    xx = 0
    yy = 25
    c1var = IntVar()
    c2var = IntVar()
    c3var = IntVar()
    c1 = Checkbutton(w9, text="All records", bg="white", variable=c1var)
    c1.place(x=xx, y=yy)
    c2 = Checkbutton(w9, text="One Record", bg="white", variable=c2var)
    c2.place(x=xx, y=yy + 20)
    c3 = Checkbutton(w9, text="Custom", bg="white", variable=c3var)
    c3.place(x=xx, y=yy + 25 + 15)
    Label(w9, text="Custom Input:", bg="white").place(x=xx, y=yy + 60)
    Custom_No = StringVar()
    Custom_Input = Entry(
        w9,
        textvariable=Custom_No,
    )
    Custom_Input.place(x=xx + 80, y=yy + 60)

    def executez():
        if c2var.get() == 1:
            curs.execute("select * from %s limit 1" % tname.get())
            ans = curs.fetchone()
            w10 = Toplevel()
            w10.resizable(0, 0)
            w10.title("Output")
            w10.config(bg="white")
            w10.iconbitmap("./IcoImages/pslogo.ico")
            Label(
                w10,
                text="Rollno",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=0)
            Label(
                w10,
                text="Name",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=1)
            Label(
                w10,
                text="Class",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=2)
            Label(
                w10,
                text="Stream",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=3)
            Label(
                w10,
                text="Section",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=4)
            Label(
                w10,
                text="Total",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=5)
            Label(
                w10,
                text=ans[0],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=0)
            Label(
                w10,
                text=ans[1],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=1)
            Label(
                w10,
                text=ans[2],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=2)
            Label(
                w10,
                text=ans[3],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=3)
            Label(
                w10,
                text=ans[4],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=4)
            Label(
                w10,
                text=ans[5],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=1, column=5)
        elif c1var.get() == 1:
            w10 = Toplevel()
            w10.resizable(0, 0)
            w10.title("Output")
            w10.config(bg="white")
            w10.iconbitmap("./IcoImages/pslogo.ico")
            Label(
                w10,
                text="Rollno",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=0)
            Label(
                w10,
                text="Name",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=1)
            Label(
                w10,
                text="Class",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=2)
            Label(
                w10,
                text="Stream",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=3)
            Label(
                w10,
                text="Section",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=4)
            Label(
                w10,
                text="Total",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=5)
            curs.execute("select * from %s" % tname.get())
            for i, records in enumerate(curs):
                Label(
                    w10,
                    text=records[0],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=0)
                Label(
                    w10,
                    text=records[1],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=1)
                Label(
                    w10,
                    text=records[2],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=2)
                Label(
                    w10,
                    text=records[3],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=3)
                Label(
                    w10,
                    text=records[4],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=4)
                Label(
                    w10,
                    text=records[5],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=5)
        elif c3var.get() == 1:
            curs.execute(
                "select * from %s limit %i" % (tname.get(), int(Custom_No.get()))
            )
            w10 = Toplevel()
            w10.resizable(0, 0)
            w10.title("Output")
            w10.config(bg="white")
            w10.iconbitmap("./IcoImages/pslogo.ico")
            Label(
                w10,
                text="Rollno",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=0)
            Label(
                w10,
                text="Name",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=1)
            Label(
                w10,
                text="Class",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=2)
            Label(
                w10,
                text="Stream",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=3)
            Label(
                w10,
                text="Section",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=4)
            Label(
                w10,
                text="Total",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=5)
            for i, records in enumerate(curs):
                Label(
                    w10,
                    text=records[0],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=0)
                Label(
                    w10,
                    text=records[1],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=1)
                Label(
                    w10,
                    text=records[2],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=2)
                Label(
                    w10,
                    text=records[3],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=3)
                Label(
                    w10,
                    text=records[4],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=4)
                Label(
                    w10,
                    text=records[5],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=5)

    submit_button = Button(
        w9,
        text="SUBMIT",
        font=("COCOGOOSE", 12),
        borderwidth=0,
        command=executez,
        fg="white",
        bg="#34822a",
    )
    submit_button.place(x=130, y=34)


def delete_rec():
    w12 = Toplevel()
    w12.resizable(0, 0)
    w12.title("Input")
    w12.iconbitmap("./IcoImages/pslogo.ico")
    w12.config(bg="white")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 254
    wh = 100
    w12.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    tname = StringVar()
    rn = StringVar()
    try:
        tname_label = Label(w12, text="Table Name:", bg="white")
        tname_label.grid(row=0, column=0)
        rn_label = Label(w12, text="Rollno:", bg="white")
        rn_label.grid(row=1, column=0)
        tname_entry = Entry(w12, textvariable=tname, width=30)
        tname_entry.grid(row=0, column=1)
        rn_entry = Entry(w12, textvariable=rn, width=30)
        rn_entry.grid(row=1, column=1)

        def execute():
            curs.execute(
                "delete from %s where rollno=%i" % (tname.get(), int(rn.get()))
            )
            messagebox.showinfo("Output", "Record Deleted Successfully")
            rn.set("")

        submit_button = Button(
            w12,
            text="SUBMIT",
            font=("COCOGOOSE", 10),
            command=execute,
            borderwidth=0,
            fg="white",
            bg="#34822a",
            padx=5,
            pady=5,
        )
        submit_button.place(x=87, y=55)
    except:
        mydb.rollback()
        print("something went wrong in delete record block")
        raise


def topperlist():
    w13 = Toplevel()
    w13.resizable(0, 0)
    w13.title("result")
    w13.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 200
    wh = 100
    w13.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    try:
        tname = StringVar()
        Label(w13, text="Table Name:").grid(row=0, column=0)
        tablename = Entry(w13, textvariable=tname)
        tablename.grid(row=0, column=1)

        def execution():
            w14 = Toplevel()
            w14.resizable(0, 0)
            w14.title("Output")
            w14.config(bg="white")
            w14.iconbitmap("./IcoImages/pslogo.ico")
            Label(
                w14,
                text="Rollno",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=0)
            Label(
                w14,
                text="Name",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=1)
            Label(
                w14,
                text="Class",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=2)
            Label(
                w14,
                text="Stream",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=3)
            Label(
                w14,
                text="Section",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=4)
            Label(
                w14,
                text="Total",
                fg="#34822a",
                bg="white",
                font=("COCOGOOSE", heading_font_size),
            ).grid(row=0, column=5)
            curs.execute("Select max(total) from %s " % tname.get())
            a = [x for x in curs]
            curs.execute("select * from %s where total=%i" % (tname.get(), a[0][0]))
            for i, records in enumerate(curs):
                Label(
                    w14,
                    text=records[0],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=0)
                Label(
                    w14,
                    text=records[1],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=1)
                Label(
                    w14,
                    text=records[2],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=2)
                Label(
                    w14,
                    text=records[3],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=3)
                Label(
                    w14,
                    text=records[4],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=4)
                Label(
                    w14,
                    text=records[5],
                    fg="#34822a",
                    bg="white",
                    font=("calibre", output_font_size),
                ).grid(row=i + 1, column=5)
            mydb.commit()

        Button(
            w13,
            text="Submit",
            font=("COCOGOOSE", 10),
            bg=green_shade,
            fg="white",
            command=execution,
            borderwidth=0,
            border=0,
        ).place(x=70, y=40)
    except:
        print("an error occurred in topperlist block")
        raise
        mydb.rollback()


def fetch_data_d():
    w9 = Toplevel()
    w9.resizable(0, 0)
    w9.title("Input")
    w9.iconbitmap("./IcoImages/pslogo.ico")
    w9.config(bg="white")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 250
    wh = 120
    w9.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    tname = StringVar()
    tname_label = Label(w9, text="Table Name:", bg="white")
    tname_label.grid(row=0, column=0)
    tname_entry = Entry(w9, textvariable=tname, width=30)
    tname_entry.grid(row=0, column=1)

    def execute():
        w10 = Toplevel()
        w10.resizable(0, 0)
        w10.title("Output")
        w10.config(bg="white")
        w10.iconbitmap("./IcoImages/pslogo.ico")
        Label(
            w10,
            text="Rollno",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=0)
        Label(
            w10,
            text="Name",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=1)
        Label(
            w10,
            text="Class",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=2)
        Label(
            w10,
            text="Stream",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=3)
        Label(
            w10,
            text="Section",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=4)
        Label(
            w10,
            text="Total",
            fg="#34822a",
            bg="white",
            font=("COCOGOOSE", heading_font_size),
        ).grid(row=0, column=5)
        curs.execute("select * from %s order by rollno desc" % tname.get())
        for i, records in enumerate(curs):
            Label(
                w10,
                text=records[0],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=0)
            Label(
                w10,
                text=records[1],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=1)
            Label(
                w10,
                text=records[2],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=2)
            Label(
                w10,
                text=records[3],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=3)
            Label(
                w10,
                text=records[4],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=4)
            Label(
                w10,
                text=records[5],
                fg="#34822a",
                bg="white",
                font=("calibre", output_font_size),
            ).grid(row=i + 1, column=5)

    submit_button = Button(
        w9,
        text="SUBMIT",
        font=("COCOGOOSE", 12),
        borderwidth=0,
        command=execute,
        fg="white",
        bg="#34822a",
    )

    submit_button.place(x=90, y=40)


# <------------------------------------- GUI ---------------------------------------------------->
# First Tkinter Window

root = Tk()
root.resizable(0, 0)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 450
wh = 300
root.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
root.iconbitmap("./IcoImages/pslogo.ico")
root.title("Student Management System")

canva = Canvas(root, width=455, height=305, bg="white", highlightthickness=0)
canva.pack()

student_logo = PhotoImage(file="./Images/student.png")
canva.create_image(350, 175, image=student_logo)
canva.create_rectangle(-1, -1, 450, 67, fill="#34822a")

# Commands available


def commandz():
    root2 = Toplevel(root)
    root2.resizable(0, 0)
    root2.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 390
    wh = 430
    root2.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    root2.minsize(390, 430)
    root2.maxsize(390, 430)
    root2.title("Commands")
    root2.config(bg="white")
    sd = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Show Databases",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=show_databases,
    )
    sd.pack(pady=3)
    st = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Show Tables",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=show_tables,
    )
    st.pack(pady=3)
    ct = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Create Table",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=create_table,
    )
    ct.pack(pady=3)
    ds = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Display Struc",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=display_Struc,
    )
    ds.pack(pady=3)
    ar = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Add Record",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=add_rec,
    )
    ar.pack(pady=3)
    ur = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Update Record",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=update_rec,
    )
    ur.pack(pady=3)
    fd = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Fetch Data",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=fetch_data,
    )
    fd.pack(pady=3)
    dr = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Delete Record",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=delete_rec,
    )
    dr.pack(pady=3)
    top = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Topperlist",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=topperlist,
    )
    top.pack(pady=3)
    fdD = Button(
        root2,
        font=("COCOGOOSE", 12),
        border=0,
        text="Fetch Data in Descending",
        borderwidth=0,
        fg="white",
        bg=green_shade,
        command=fetch_data_d,
    )
    fdD.pack(pady=3)
    root2.mainloop()

    def colorchange(i):
        def color_change1(e):
            i["bg"] = "white"
            i["fg"] = green_shade

        def color_change2(e):
            i["bg"] = green_shade
            i["fg"] = "white"

        i.bind("<enter>", color_change1)
        i.bind("<Leave>", color_change2)

    l = [st, sd, ds, ct, fdD, top, dr, fd, ur, ar]
    for i in l:
        colorchange(i)


# ------------- Authentication ---------


def verification():

    root3 = Toplevel()
    root3.resizable(0, 0)
    root3.title("Authentication")
    root3.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 250
    wh = 100
    root3.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    root3.config(bg="white")

    def checkU_P():
        userv = user.get()
        passv = Pass.get()
        with open("userpass.dat", "rb") as upfile:
            u = load(upfile)
            if userv == u[0] and passv == u[1]:
                root3.destroy()
                commandz()
            else:
                messagebox.showwarning("Warning!", "username or password is incorrect!")

    user = StringVar()
    Pass = StringVar()
    user_label = Label(root3, text="Username:", bg="white")
    user_label.grid(row=0, column=0)
    pass_label = Label(root3, text="Password:", bg="white")
    pass_label.grid(row=1, column=0)
    user_entry = Entry(root3, textvariable=user, width=30)
    user_entry.grid(row=0, column=1)
    Pass_entry = Entry(root3, textvariable=Pass, show="*", width=30)
    Pass_entry.grid(row=1, column=1)
    submit_button = Button(
        root3,
        text="SUBMIT",
        font=("COCOGOOSE", 10),
        command=checkU_P,
        borderwidth=0,
        fg="white",
        bg="#34822a",
    )
    submit_button.place(x=95, y=50)


def settings():
    heading_font_size_entry = StringVar()
    output_font_size_entry = StringVar()

    settings_window = Toplevel()
    settings_window.resizable(0, 0)
    settings_window.title("Settings")
    settings_window.iconbitmap("./IcoImages/pslogo.ico")
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    ww = 310
    wh = 100
    settings_window.geometry(f"{ww}x{wh}+{int(sw / 2 - ww / 2)}+{int(sh / 2 - wh / 2)}")
    Label(settings_window, text="Field Name Font Size:", font=("calibre", 11)).grid(
        row=1, column=0
    )
    Label(settings_window, text="Record Name Font Size:", font=("calibre", 11)).grid(
        row=2, column=0
    )
    Entry(settings_window, textvariable=heading_font_size_entry).grid(row=1, column=1)
    Entry(settings_window, textvariable=output_font_size_entry).grid(row=2, column=1)

    def executez():
        if heading_font_size_entry != "":
            global heading_font_size
            heading_font_size = heading_font_size_entry.get()
        elif heading_font_size == "":
            pass
        if output_font_size_entry != "":
            global output_font_size
            output_font_size = output_font_size_entry.get()
        elif output_font_size_entry == "":
            pass
        messagebox.showinfo("Attention!", "All Changes Saved")

    Button(
        settings_window,
        text="Submit",
        font=("COCOGOOSE", 11),
        fg="white",
        bg=green_shade,
        command=executez,
        border=0,
        borderwidth=0,
    ).place(x=115, y=60)


if master_key == True:
    com = commandz
else:
    com = verification

# Second window
admin_label = Label(
    root, text="WELCOME", font=("COCOGOOSE", 36), fg="white", bg="#34822a", padx=200
)
admin_label.place(x=-103, y=-1)
next_X = 172
next_Y = 120
next_label = Label(root, text="Next", font="COCOGOOSE 23", fg="#34822a", bg="white")
next_label.place(y=next_Y + 3, x=next_X - 90)
nextbimage = PhotoImage(file="./Images/next.png")
nextb = Button(root, image=nextbimage, borderwidth=0, command=com, bg="white")
nextb.place(x=next_X, y=next_Y, width=50, height=50)
crossbimage = PhotoImage(file="./Images/cross.png")
crossb = Button(
    root, image=crossbimage, borderwidth=0, command=root.destroy, bg="white"
)
crossb.place(x=next_X, y=next_Y + 65, width=50, height=50)
exit_label = Label(root, text="Exit", font=("COCOGOOSE", 23), fg="#34822a", bg="white")
exit_label.place(x=next_X - 70, y=next_Y + 68)
name = " Developed by Prabhjot Singh"
name_label = Label(root, text=name, fg="black", bg="white", font=("Prompt Light", 10))
name_label.place(x=-4, y=280)
message = " [Click the circular buttons to proceed or exit]"
message_label = Label(
    root, text=message, fg="#34822a", bg="white", font=("Prompt Light", 8)
)
message_label.place(x=88, y=68)
settings_image = PhotoImage(file="./Images/gear.png")
settings_button = Button(
    root, image=settings_image, borderwidth=0, command=settings, bg="white"
).place(x=425, y=274)
# mainloop
root.mainloop()
