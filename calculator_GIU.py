#version 1
from tkinter import *
win = Tk()
win.geometry('230x248')
win.title('Calculator')
def but1f():
    ent1.insert(END, 1)
def but2f():
    ent1.insert(END, 2)
def but3f():
    ent1.insert(END, 3)
def but4f():
    ent1.insert(END, 4)
def but5f():
    ent1.insert(END, 5)
def but6f():
    ent1.insert(END, 6)
def but7f():
    ent1.insert(END, 7)
def but8f():
    ent1.insert(END, 8)
def but9f():
    ent1.insert(END, 9)
def but0f():
    ent1.insert(END, 0)
def read():
    a = ent1.get()
    text1.delete(0.0, END)
    text1.insert(END, eval(a))
def butpf():
    ent1.insert(END, '+')
def butmf():
    ent1.insert(END, '-')
def butsf():
    ent1.insert(END, '(')
def butssf():
    ent1.insert(END, ')')
def butyf():
    ent1.insert(END, '*')
def butdf():
    ent1.insert(END, '/')
def butddf():
    ent1.insert(END, '//')
def butdof():
    ent1.insert(END, '%')
def delt():
    a = ent1.get()
    str(a)
    ent1.delete(int(len(a))-1, END)

but1 = Button(text='   1   ', command=but1f, fg='black', activebackground='gold', bg='cyan')
but1.grid(columnspan=2, rowspan=2)
but1.place(x=20, y=25)
but2 = Button(text='   2   ', command=but2f, fg='black', activebackground='gold', bg='cyan')
but2.grid(columnspan=2, rowspan=2)
but2.place(x=60, y=25)
but3 = Button(text='   3   ', command=but3f, fg='black', activebackground='gold', bg='cyan')
but3.grid(columnspan=2, rowspan=2)
but3.place(x=100, y=25)
but4 = Button(text='   4   ', command=but4f, fg='black', activebackground='gold', bg='cyan')
but4.grid(columnspan=2, rowspan=2)
but4.place(x=20, y=50)
but5 = Button(text='   5   ', command=but5f, fg='black', activebackground='gold', bg='cyan')
but5.grid(columnspan=2, rowspan=2)
but5.place(x=60, y=50)
but6 = Button(text='   6   ', command=but6f, fg='black', activebackground='gold', bg='cyan')
but6.grid(columnspan=2, rowspan=2)
but6.place(x=100, y=50)
but7 = Button(text='   7   ', command=but7f, fg='black', activebackground='gold', bg='cyan')
but7.grid(columnspan=2, rowspan=2)
but7.place(x=20, y=75)
but8 = Button(text='   8   ', command=but8f, fg='black', activebackground='gold', bg='cyan')
but8.grid(columnspan=2, rowspan=2)
but8.place(x=60, y=75)
but9 = Button(text='   9   ', command=but9f, fg='black', activebackground='gold', bg='cyan')
but9.grid(columnspan=2, rowspan=2)
but9.place(x=100, y=75)
but0 = Button(text='   0   ', command=but0f, fg='black', activebackground='gold', bg='cyan')
but0.grid(columnspan=2, rowspan=2)
but0.place(x=20, y=100)
but11 = Button(text='     Ready!     ', command=read, fg='black', activebackground='OrangeRed', bg='red')
but11.grid(columnspan=2, rowspan=2)
but11.place(x=60, y=100)
ent1 = Entry()
ent1.grid()
ent1.place(x=50, y=0)
text1 = Text(height=5, width=15)
text1.grid()
text1.place(x=50, y=160)
but12 = Button(text='   +  ', command=butpf, fg='black', activebackground='green', bg='SpringGreen2')
but12.grid(columnspan=2, rowspan=2)
but12.place(x=140, y=50)
but13 = Button(text='   -   ', command=butmf, fg='black', activebackground='green', bg='SpringGreen2')
but13.grid(columnspan=2, rowspan=2)
but13.place(x=180, y=50)
but14 = Button(text='   *   ', command=butyf, fg='black', activebackground='green', bg='SpringGreen2')
but14.grid(columnspan=2, rowspan=2)
but14.place(x=140, y=75)
but15 = Button(text='   /   ', command=butdf, fg='black', activebackground='green', bg='SpringGreen2')
but15.grid(columnspan=2, rowspan=2)
but15.place(x=180, y=75)
but16 = Button(text='   (   ', command=butsf, fg='black', activebackground='green', bg='SpringGreen2')
but16.grid(columnspan=2, rowspan=2)
but16.place(x=140, y=24)
but17 = Button(text='    )  ', command=butssf, fg='black', activebackground='green', bg='SpringGreen2')
but17.grid(columnspan=2, rowspan=2)
but17.place(x=180, y=24)
but18 = Button(text='  //  ', command=butddf, fg='black', activebackground='green', bg='SpringGreen2')
but18.grid(columnspan=2, rowspan=2)
but18.place(x=140, y=100)
but19 = Button(text='  %  ', command=butdof, fg='black', activebackground='green', bg='SpringGreen2')
but19.grid(columnspan=2, rowspan=2)
but19.place(x=180, y=100)
but20 = Button(text='                         <--                              ', command=delt)
but20.grid(columnspan=2, rowspan=2)
but20.place(x=20, y=125)





win.mainloop()