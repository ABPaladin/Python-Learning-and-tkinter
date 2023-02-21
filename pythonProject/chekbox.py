import tkinter as tk

win = tk.Tk()
win.geometry('500x500')

over_18_value=tk.StringVar()
over_18_value.set('no')
over_18 = tk.Checkbutton(win, text='I am 18',variable=over_18_value, onvalue='yes',offvalue='off')
over_18.pack()

def show():
    print(over_18_value.get())
def select_all():
        for check in [over_18,agree,ad]:
            check.select()

def deselect_all():
    for check in [over_18, agree, ad]:
        check.deselect()

def toggle():
    for check in [over_18,agree,ad]:
        check.toggle()

agree = tk.Checkbutton(win, text='I agree to licence terms')
agree.pack()
ad = tk.Checkbutton(win, text='I want to get ads')
ad.pack()

tk.Button(win, text='selcet all', command=select_all).pack()
tk.Button(win, text='deselcet all', command=deselect_all).pack()
tk.Button(win, text='toggle', command=toggle).pack()
tk.Button(win, text='show', command=show).pack()


win.mainloop()