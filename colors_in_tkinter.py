#in tkinter there are 256^3 i.e. 16 million colors 
#only we have a fear related to hexa color code
#well is it very to get how it works
#so it used RGB color scheme
#RGB(vR,vG,vB), where vR,vG,vB are the value used in color code ranges form 0 to 255
# in hex it is =>"#VrVgVb" where Vr,Vg,Vb in hex i.e. ranges from 00 to FF

from tkinter import *
from random import randint, randrange

def getcode(code):
    label.configure(text="The Hex Color Code is {}".format(code),font=("Arial",30))

#note that r,g,b are in persentage due to with we will multiply with 2.55 i.e.255/100=>2.55
def color_convert(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(int(r*2.55),int(g*2.55),int(b*2.55))

def random_color():
    r,g,b=randint(0,100),randint(0,100),randint(0,100)
    return color_convert(r,g,b)

#text
print(color_convert(10,20,40))
root=Tk()
root.title("Colors pad")
root.geometry("500x500")
#let's make a buttons with different colors
color=[0]*100
k=0
label=Label()
label.grid(row=0,column=0,columnspan=10)
for i in range(1,11):
    for j in range(1,11):
        hexcode=color_convert(randint(0,100),randint(0,100),randint(0,100))
        color[k]=Button(text=str(k+1),bg=hexcode,width=10,command=lambda x=hexcode:getcode(x))
        color[k].grid(row=i,column=j)
        k+=1

mainloop()

