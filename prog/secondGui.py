from tkinter import *
import time

def getdata():
   

    x=0;
    while x<10:
        x=x+1
        time.sleep(10)
        text.insert(0.0, "dkjdfkj"+str("\n"))
        



root = Tk()
root.geometry("400x500")

l1=Label(root, text="name")
l2= Label(root, text="Gender")
ent=Entry(root)
var_g=IntVar()

rd1 = Radiobutton(root, text="male",variable=var_g, value=1)
rd2 = Radiobutton(root, text="female",variable=var_g, value=2)

l1.grid(row=0)
l2.grid(row=1)

ent.grid(row=0)

rd1.grid(row=1,column=1,sticky=W)
rd2.grid(row=1,column=1,sticky=E)

btn=Button(root, text="getData", command=getdata) 
btn.grid(row=2,columnspan=2)

text=Text(root, width=30, height=10, wrap=WORD)
text.grid(row=3, columnspan=2, sticky=W)

root.mainloop()
