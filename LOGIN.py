from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

db = mysql.connector.connect(
            host="localhost",
            user="JVM",
            passwd="JVM_2001",
            auth_plugin='caching_sha2_password',
            database="test_login_details"
        )
my_cursor = db.cursor(dictionary=True)


def login_message():
    my_cursor.execute("SELECT * FROM user_details")
    records = my_cursor.fetchall()
    username = E.get()  # Getting User_name from the Username-Entry
    password = E1.get()  # Getting Password from the Password-Entry
    E.delete(0, END)
    E1.delete(0, END)
    count = 0
    flag = 0
    for x in records:
        count += 1   # To obtain Max records from table
    for table in records:
        username_from_table = table["username"]
        password_from_table = table["passwrd"]
        if (username_from_table != username) and (password_from_table != password):
            flag += 1
        elif (username_from_table == username) and (password_from_table == password):
            messagebox.showinfo("Login", "Login Successful")
            break

    if flag == count:  # If MAX_RECCORD IS EQUAL TO flag variable no record found
        messagebox.showerror("Login", "Invalid Details")


def new_register():
    root1 = Tk()
    root1.title("Passport Application")
    root1.iconbitmap("D:/GIT_PROJECT/MINI_PROJECT/images/ico/flight.ico")

    root1.mainloop()


root = Tk()
root.title("Passport Application")
root.iconbitmap("D:/GIT_PROJECT/MINI_PROJECT/images/ico/flight.ico")
root.geometry("1366x768")
img = ImageTk.PhotoImage(Image.open("D:/GIT_PROJECT/MINI_PROJECT/images/flight.png"))
my_img = Label(image=img).grid(padx=50, pady=5, sticky=S)
frame = LabelFrame(root, padx=350, pady=50)
frame.grid(padx=85, pady=40)

# User-Name Index
UserName_label = Label(frame, text="UserName:*", padx=2, pady=5, justify=RIGHT, font=("Times", 14, "bold")).grid(row=0, column=0, padx=1, pady=5)
E = Entry(frame, width=50, borderwidth=3, bg="#DCDCDC")
E.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

# Password_Index
Password_label = Label(frame, text="Password:*", padx=2, pady=5, justify=RIGHT, font=("Times", 14, "bold")).grid(row=1, column=0, padx=1, pady=5)
E1 = Entry(frame, width=50, borderwidth=3, bg="#DCDCDC",  show="*")
E1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# BUTTONS -Submit & -New_User
lg_button = PhotoImage(file='D:/GIT_PROJECT/MINI_PROJECT/images/login.png')
Submit_Button = Button(frame, image=lg_button, padx=10, pady=5, borderwidth=4, command=login_message, cursor="hand2", bd=0)
Submit_Button.grid(row=2, column=2, padx=30, pady=10)

reg_button = PhotoImage(file='D:/GIT_PROJECT/MINI_PROJECT/images/register.png')
New_User_Button = Button(frame,  image=reg_button, padx=5, pady=5, borderwidth=4, command=new_register, cursor="hand2", bd=0)
New_User_Button.grid(row=3, column=2, padx=30, pady=5)

root.mainloop()
