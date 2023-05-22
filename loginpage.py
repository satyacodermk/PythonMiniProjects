#designing the loging page using tkinter module 
from logging import PlaceHolder
import tkinter as tk
from traceback import format_tb
from turtle import pos

root=tk.Tk()
root.resizable(width=700,height=800)
root.title("Login Page")
root.configure(bg="black")
font=('Verdana',50)
label1=tk.Label(root,text="Please Login to the page",font=font,fg="blue",bg="black",padx=50,pady=20)
label1.place(relx=0.5,rely=0.1,anchor="center")
#label.grid(row=0,column=0)
label2=tk.Label(root,text="Enter your name",font=("Helvetica",20),fg="white",bg="black")
label2.place(relx=0.3,rely=0.3,anchor="center")
ent1=tk.Entry(root,font=("Arial",14),fg="blue",bg="aqua")
ent1.place(relx=0.5,rely=0.3,anchor='center')


#label.grid(row=0,column=0)
label3=tk.Label(root,text="Enter Password ",font=("Helvetica",20),fg="white",bg="black")
label3.place(relx=0.3,rely=0.4,anchor="center")
ent2=tk.Entry(root,font=("Arial",14),fg="blue",bg="aqua")
ent2.place(relx=0.5,rely=0.4,anchor='center')


#radio button

male=tk.Checkbutton(root,text="Male",bg="black",fg="white",font=("Arial",15))
Female=tk.Checkbutton(root,text="Female",bg="black",fg="white")
male.place(relx=0.3,rely=0.44)

but=tk.Button(root,bg="blue",fg="yellow")
but.configure(text="Submit",font=("Arial",14))
but.place(relx=0.5,rely=0.5,anchor="center")
tk.mainloop()