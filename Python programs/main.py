# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

def func(a,b,x=True):
    s = a + b
    if x:
        s +=10
    return s
def suma(a,b):
    return a + b

print(func(4,5,True))
print(func(4,5,False))
print(suma(3,12))
print(suma("Hello", " World"))