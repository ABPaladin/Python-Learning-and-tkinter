# from tkinter import *
#
# win = Tk()
#
# button_quit = Button(win, text="Exit program", command=win.quit())
# button_quit.pack()
#
# win.mainloop()

from tkinter import *
from tkinter import filedialog

def saveFile():
    file_name = filedialog.asksaveasfilename(initialdir='/',title='select file',filetypes=(('Text Documents','*.txt'),('All files','*.*')))
    if file_name:
        f = open(file_name, 'w')
        text_save = str(text.get(1.0,END))
        f.write(text_save+"\n")
        f.close()

def openFile():
    file_name = filedialog.askopenfilename(initialdir='/', title='select file',filetypes=(('Text Documents', '*.txt'), ('All files', '*.*')))
    if file_name:
        f = open(file_name, 'r')
        text_open = f.read()
        if text_open != NONE:
            text.delete(1.0,END)
            text.insert(END,text_open)
win = Tk()

menu = Menu(win)
win.config(menu=menu)

file_menu=Menu(menu, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Open', command=openFile)
file_menu.add_command(label='Save as..', command=saveFile)
file_menu.add_command(label='Exit', command=exit)

help_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Help')
help_menu.add_command(label='About')

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Help', menu=help_menu)

text = Text(win)
text.pack(expand=YES, fill=BOTH)

win.mainloop()