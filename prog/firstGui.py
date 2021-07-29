import tkinter as tk
from tkinter import *
r = tk.Tk()
# r.title('Scrolling')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
# root = Tk()
scrollbar = Scrollbar(r)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(r, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, 'This is line number' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()