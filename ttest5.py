import tkinter as tk
import tkinter.messagebox as msg
w = tk.Tk()
w.title("Calculator")
w.geometry("500x400+400+100")
w.config(bg="cyan")
l1 = tk.Label(w,text="Number1 : ",bg='cyan',fg='red',font=('Arial',14))
e1 = tk.Entry(w,font=('Arial',14),bg='yellow',fg='blue')
l1.place(x=100,y=50)
e1.place(x=200,y=50)
l2 = tk.Label(w,text="Number2 : ",bg='cyan',fg='red',font=('Arial',14))
e2 = tk.Entry(w,font=('Arial',14),bg='yellow',fg='blue')
l2.place(x=100,y=100)
e2.place(x=200,y=100)
l3 = tk.Label(w,text="Result  : ",bg='cyan',fg='red',font=('Arial',14))
e3 = tk.Entry(w,font=('Arial',14),bg='yellow',fg='blue')
l3.place(x=100,y=150)
e3.place(x=200,y=150)
def add():
    try:
        v1 = eval(e1.get())
        v2 = eval(e2.get())
        v3 = v1+v2
        e3.delete(0,tk.END)
        e3.insert(0,str(v3))
    except:
        msg.showinfo(title="Error",message="Enter integer values only")



def sub():
    try:
        v1 = eval(e1.get())
        v2 = eval(e2.get())
        v3 = v1-v2
        e3.delete(0,tk.END)
        e3.insert(0,str(v3))
    except:
        msg.showinfo(title="Error",message="Enter integer values only")


def mul():
    try:
        v1 = eval(e1.get())
        v2 = eval(e2.get())
        v3 = v1*v2
        e3.delete(0,tk.END)
        e3.insert(0,str(v3))
    except:
        msg.showinfo(title="Error",message="Enter integer values only")
def div():
    try:
        v1 = eval(e1.get())
        v2 = eval(e2.get())
        v3 = v1/v2
        e3.delete(0,tk.END)
        e3.insert(0,str(v3))
    except:
        msg.showinfo(title="Error",message="Enter integer values only or Cannot divide by Zero")


b1 = tk.Button(w,text="ADD",font=('Arial',14),bg="black",fg="white",command=add,width=10)
b2 = tk.Button(w,text="SUB",font=('Arial',14),bg="black",fg="white",command=sub,width=10)
b3 = tk.Button(w,text="MUL",font=('Arial',14),bg='black',fg='white',command=mul,width=10)
b4 = tk.Button(w,text="DIV",font=('Arial',14),bg='black',fg='white',command=div,width=10)
b5 = tk.Button(w,text="Exit",font=('Arial',14),bg='black',fg='white',command=lambda:w.destroy(),width=10)


b1.place(x=120,y=200)
b2.place(x=270,y=200)
b3.place(x=120,y=250)
b4.place(x=270,y=250)
b5.place(x=190,y=300)
