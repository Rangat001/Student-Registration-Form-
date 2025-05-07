from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y)


root.title("fun")
root.geometry("500x400")



# label
Label(root, text="Student Registration Form", font="arial 16 bold", fg="red", bg="lightpink").place(x=500, y=10)

Label(root, text="Enter Your Name: ", fg="red").place(x=40, y=70)

Label(root, text="Enter Your Phone Number: ", fg="red").place(x=40, y=130)

Label(root, text="Enter Your Enrollment: ", fg="red").place(x=40, y=190)

Label(root, text="Enter Your Email Id: ", fg="red").place(x=40, y=250)

Label(root, text="Sem: ", fg="red").place(x=400, y=310)

Label(root, text="Department: ", fg="red").place(x=750, y=310)

Label(root, text="Gender: ", fg="red").place(x=40, y=370)

Label(root, text="Date Of Birth: ", fg="red").place(x=40, y=430)

Label(root, text="Course: ", fg="red").place(x=40, y=310)


# entry
name = StringVar()
phone = StringVar()
enroll = StringVar()
email = StringVar()
entry1 = Entry(root, bg="yellow", fg="blue",)
entry1.place(x=40, y=95)
entry2 = Entry(root, bg="yellow", fg="blue")
entry2.place(x=40, y=155)
entry3 = Entry(root, bg="yellow", fg="blue")
entry3.place(x=40, y=215)
entry4 = Entry(root, bg="yellow", fg="blue")
entry4.place(x=40, y=275)

cmb1= ttk.Combobox(root, value=(1, 2, 3, 4, 5, 6), state="readonly", width=10)
cmb1.place(x=400, y=335)

cmb2 = ttk.Combobox(root, value=("IT", "Electrical", "EC", "Civil", "Mechanical", "Automobile", "Plastic"),state="readonly", width=10)
cmb2.place(x=750, y=335)


cmb3 = ttk.Combobox(root, value=(
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31),state="readonly", width=10)
cmb3.place(x=40, y=455)


cmb4 = ttk.Combobox(root,
                   value=("Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"),
                   state="readonly", width=10)
cmb4.place(x=380, y=455)

cmb5 = ttk.Combobox(root, value=(
2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
2020, 2021, 2022), state="readonly", width=10)
cmb5.place(x=700, y=455)

cmb6 = ttk.Combobox(root, value=(
"DIPL", "DEGREE", "BE", "ME", "B.FARM", "M.FARM", "MSC", "MSC In Biotech", "B Arch", "MBA", "Other"), state="readonly",width=10)
cmb6.place(x=40, y=335)

# radiobtn
gender = StringVar()
male1 = Radiobutton(root, value="Boy", text="Boy", variable=gender)
male1.place(x=100, y=370)

female1 = Radiobutton(root, value="Girl", text="Girl", variable=gender)
female1.place(x=160, y=370)


# button


def fun():
    name1 = entry1.get()
    phone2 = entry2.get()
    enroll3 = entry3.get()
    email4 = entry4.get()
    sem= cmb1.get()
    Department=cmb2.get()
    course= cmb6.get()
    date= cmb3.get()
    month= cmb4.get()
    year= cmb5.get()
    male1=gender.get()
    
    if name1 == "":
      	messagebox.showerror("Error", "pls enter your name")
    elif phone2 == "":
        messagebox.showerror("Error", "pls enter your phone")
    elif enroll3 == "":
        messagebox.showerror("Error", "pls enter your enroll")
    elif email4 == "":
        messagebox.showerror("Error", "pls enter your email")
    else:
        Label(root, text="Login Succefull",fg="green").place(x=430, y=550)

        f = open("Student Registration Form.txt", "a")
        f.write("name: "+name1 +"\n")
        f.write("phone: "+phone2 + "\n")
        f.write("enrollment: "+enroll3 + "\n")
        f.write("Email: "+email4 + "\n")
        f.write("Sem: "+sem + "\n")
        f.write("course: "+course+ '\n')
        f.write("Department: "+Department+ "\n")
        f.write("Date Of Birth: "+date+"-")
        f.write(month+"-")
        f.write(year+"\n")
        f.write("gender: "+male1+"\n")
        f.write("----------------------------------------------------------")
        f.close()

Button(root, text="Login", command=fun,bg="grey",cursor="hand2").place(x=450, y=520)

root.mainloop()
