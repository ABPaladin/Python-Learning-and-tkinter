import tkinter as tk

win = tk.Tk()
win.geometry('500x500')

def select():
    for check in [over_18, agree, ad,like]:
        check.select()
def toggle():
    for check in [over_18,agree,ad,like]:
        check.toggle()
def show():
    print(over_18_value.get())
    if over_18_value.get() == 'yes':
        print("Greate your 18 congratuliasions")
    else:
        print("Your to lil kid go to your momy")


over_18_value=tk.StringVar()
over_18_value.set('no')
over_18 = tk.Checkbutton(win, text='I am 18',variable=over_18_value, onvalue='yes',offvalue='no')
over_18.pack()

agree = tk.Checkbutton(win, text='I agree to licence terms')
agree.pack()

ad = tk.Checkbutton(win, text='I want to get ads')
ad.pack()

like = tk.Checkbutton(win, text='Do you like our company')
like.pack()

tk.Button(win, text='selcet', command=select).pack()
tk.Button(win, text='toggle', command=toggle).pack()
tk.Button(win, text='show', command=show).pack()


win.mainloop()