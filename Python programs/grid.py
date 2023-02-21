import tkinter as tk

win = tk.Tk()
win.geometry("500x500")

# btn1 = tk.Button(win, text="Hello1")
# btn2 = tk.Button(win, text="Hello2")
# btn3 = tk.Button(win, text="Hello3")
# btn4 = tk.Button(win, text="Hello4")
# btn5 = tk.Button(win, text="Hello5")
# btn6 = tk.Button(win, text="Hello6")
# btn7 = tk.Button(win, text="Hello7")
# btn8 = tk.Button(win, text="Hello8")
#
# btn1.grid(row=0,column=0,stick="we")
# btn2.grid(row=0,column=1,stick="we")
# btn3.grid(row=1,column=0,stick="we")
# btn4.grid(row=1,column=1,stick="we")
# btn5.grid(row=2,column=0,stick="we")
# btn6.grid(row=2,column=1,stick="we")
# btn7.grid(row=3,column=0, columnspan=2, stick="we")
# btn8.grid(row=0,column=2, rowspan=4, stick="ns")
#
# win.grid_columnconfigure(0, minsize=200)
# win.grid_columnconfigure(1, minsize=100)

btn1 = tk.Button(win, text="Hello1")
btn2 = tk.Button(win, text="Hello2")
btn3 = tk.Button(win, text="Hello3")
btn4 = tk.Button(win, text="Hello4")
btn5 = tk.Button(win, text="Hello5")
btn6 = tk.Button(win, text="Hello6")
btn7 = tk.Button(win, text="Hello7")
btn8 = tk.Button(win, text="Hello8")

btn1.grid(row=0,column=0,rowspan=2,columnspan=2,stick="nswe")
btn2.grid(row=0,column=2)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0,columnspan=3,stick="we")
btn5.grid(row=3,column=0,stick="we")
btn6.grid(row=3,column=1,stick="we")
btn7.grid(row=3,column=2,stick="we")
btn8.grid(row=0,column=3,rowspan=4,stick="ns")


win.mainloop()

