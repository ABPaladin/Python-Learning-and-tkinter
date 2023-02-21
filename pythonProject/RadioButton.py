import tkinter as tk

win = tk.Tk()
win.geometry('500x500')

levelVar = tk.IntVar()
level_text  = tk.StringVar()

def select_levle():
    level = levelVar.get()
    s=f'you chose {level} level'
    level_text.set(s)
    if  level ==1:
        print('Easy')
    elif  level ==2:
        print('Medium')
    else:
        print('Hard')
tk.Label(win, text='dificulty level')
tk.Radiobutton(win, text='easy',variable=levelVar, value=1,command=select_levle).pack()
tk.Radiobutton(win, text='medium',variable=levelVar, value=2,command=select_levle).pack()
tk.Radiobutton(win, text='hard',variable=levelVar, value=3,command=select_levle).pack()
tk.Label(win, textvariable=level_text).pack()




win.mainloop()