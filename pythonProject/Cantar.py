from tkinter import *
# Cream Fereastra
window = Tk()
# Functia default pentru KG
def from_kg():
# Toate tipurile de marimi
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
# Crearea inputului si outputului marimiea conditia
e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
# Introducerea si crearea feresterei de text
t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
# Crearea butonului care va calcula kg in alte masuri prin cheemarea functiei "from_kg"
b1 = Button(window, text="Convert", command=from_kg)
# Crearea gridului prin grid noi aliniem si controlam cum va fi afisat fiecare element in aplicatie
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)
# Prin metoda mainloop noi pornim programul.
window.mainloop()