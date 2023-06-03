import mysql.connector
import re
from tkinter import *
from tkinter import messagebox
from subprocess import call
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
import test
def Ok():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="alan"
    )
    loaded_model = tf.keras.models.load_model("bert_model.h5", custom_objects={'KerasLayer': hub.KerasLayer})
    user_input = e2.get()
    predictions = loaded_model.predict([user_input])
    predicted_label = "Positive" if predictions[0][0] > 0.5 else "Negative"
    print("Predicted Label:", predicted_label)
    if predicted_label == "Positive":
        test.mail()
        messagebox.showinfo("", "Incorrent Username and Password")
        return False

    else:
        cursor = db.cursor()
        sql = "SELECT * FROM login WHERE admin='" + e1.get() + "' AND pass='" + e2.get() + "'"
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            messagebox.showinfo("", "Login Success")

            call(["python", "Main.py"])
            newW = Tk()
            newW.title("Stuedent Detail")
            newW.geometry("550x400")

            exe = "SELECT Name FROM stinfo where Name='" + e1.get() + "'"
            cursor.execute(exe)
            res = cursor.fetchall()
            Label(newW, text="STUDENT DETAILS", relief=RAISED, background="light blue").place(x=10, y=10)
            Label(newW, text="NAME:").place(x=30, y=50)
            Label(newW, text="res").place(x=160, y=50)

            def full():

                newW.destroy()
                r.destroy()
                Button(newW, text="Exit", command=full, height=2, width=10).place(x=450, y=350)
                Button(newW, text="Deactivate", command='del', height=2, width=10).place(x=350, y=350)
                return True

        else:
            messagebox.showinfo("", "Incorrent Username and Password")
            return False


r = Tk()
r.title("Login")
r.geometry("500x300")


def show_password():
    """Toggle the password visibility"""
    if e2.cget('show') == '':
        e2.config(show='*')
        show_password_button.config(text='Show Password')
    else:
        e2.config(show='')
        show_password_button.config(text='Hide Password')


global el, e2, p1, p2, p3, p4, p5, p6, p7, p8
global c1, c2, c3
Label(r, text="UserName").place(x=10, y=40)
Label(r, text="Password").place(x=10, y=80)
show_password_button = Button(r, text='Show Password', command=show_password)
show_password_button.pack(pady=2)
show_password_button.place(x=280, y=80)
e1 = Entry(r)
e1.place(x=140, y=50)
e2 = Entry(r)
e2.place(x=140, y=80)
e2.config(show="*")
Label(r, text="WELCOME", font=('Courier', 14, 'bold'), foreground="#0e6ea6").place(x=200, y=10)
Button(r, text="Login", command=Ok, height=1, width=10).place(x=30, y=140)
Button(r, text="Exit", command=r.destroy, height=1, width=10).place(x=120, y=140)
r.mainloop()
