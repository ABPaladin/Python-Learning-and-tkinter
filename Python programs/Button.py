import tkinter as tk

win = tk.Tk()
win.geometry("500x500")
lable1 = tk.Label(win, text="Hello")
lable2 = tk.Label(win, text="World")
lable1.pack()
lable2.pack()
def say_hello():
    print("Hello")

def add_lable():
    lable = tk.Label(win, text="new")
    lable.pack()

def counter():
    global count
    count += 1
    btn3["text"] = f"Count:{count}"

def disable():
    btn3["state"] = tk.DISABLED

def delete():
    lable1["text"] = ""
    lable2["text"] = ""

btn = tk.Button(win, text="Hello", command=say_hello)
btn.pack()

btn2 = tk.Button(win, text="add new lable", command=add_lable)
btn2.pack()

count = 0
btn3 = tk.Button(win, text=f"Count:{count}", command=counter,
                 activebackground="blue",
                 bg="red",
                 state=tk.NORMAL
                 )
btn3.pack()

btn4 = tk.Button(win, text="Disable btn3", command=disable,)
btn4.pack()

btn5 = tk.Button(win, text="delete", command=delete,)
btn5.pack()

win.mainloop()










