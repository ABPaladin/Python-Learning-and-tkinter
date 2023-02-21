import tkinter as tk


def add_digit(digit):
    value = calc.get()+str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def make_button(digit):
    return tk.Button(text=digit, font=('Arial, 13'), command=lambda: add_digit(digit))
def make_operation(op):
    return tk.Button(text=op, font=('Arial, 13'),
                     command=lambda: add_digit(op))
def make_calc_btn(op):
    return tk.Button(text=op, font=('Arial, 13'),
                     command=calculate)
def calculate():
    value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0, eval(value))

def add_opertation(op):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
        calc.delete(0,tk.END)
        calc.insert(0,value+op)
win = tk.Tk()
win.geometry('240x260+100+200')
win['bg'] = '#E6F9EF'
win.title('Calculator')

calc = tk.Entry(win, font=('Arial, 13'), width=15, justify=tk.RIGHT)
calc.grid(row=0,column=0,columnspan=3, stick='we')

make_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_button('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)

make_operation('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_btn('=').grid(row=0, column=3, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()





# import tkinter as tk
#
# def get_entry():
#     value = name.get(),surname.get(),password.get(),gender.get()
#     if value:
#         tk.Label(win, text=value).grid(row=9, column=1)
#     else:
#         print("Empty entry")
#
# def delete_entry():
#     name.delete(0, tk.END),surname.delete(0, tk.END),password.delete(0, tk.END),gender.delete(0, tk.END)
# def insert_entry():
#     name.insert(0, "hello"),surname.insert(0,"bye"),password.insert(0,"1234"),gender.insert(0,"Unknon")
#
# def get_gender_m():
#     gender.insert(3, "man")
# def get_gender_f():
#     gender.insert(3, "woman")
#
#
# win = tk.Tk()
# win.geometry("500x500")
# name = tk.Entry(win)
# name.grid(row=0,column=1)
# surname = tk.Entry(win)
# surname.grid(row=1,column=1)
# password = tk.Entry(win, show='*')
# password.grid(row=2, column=1)
# gender = tk.Entry(win)
# gender.grid(row=3, column=1)
#
# tk.Label(win, text="Enter your name").grid(row=0, column=0)
# tk.Label(win, text="Enter your Surname").grid(row=1, column=0)
# tk.Label(win, text="Enter your Password").grid(row=2, column=0)
# tk.Label(win, text="Gender").grid(row=3, column=0)
# tk.Button(win, text="M",command=get_gender_m).grid(row=3, column=3, columnspan=2)
# tk.Button(win, text="F",command=get_gender_f).grid(row=3, column=6, columnspan=2)
# tk.Button(win, text="Submit", command=get_entry).grid(row=4, column=1, columnspan=2)
# tk.Button(win, text="Delete", command=delete_entry).grid(row=5, column=1, columnspan=2)
# tk.Button(win, text="Insert", command=insert_entry).grid(row=6,column=1,columnspan=2)
#
# win.mainloop()

