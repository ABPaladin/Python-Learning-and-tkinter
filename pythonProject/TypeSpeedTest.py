from tkinter import *
import ctypes
import random
import tkinter

# pentru o fereastra mai ascutita
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Punem Baza
root = Tk()
root.title('Type Speed Test')

# Punem Dimensiunile la fereastra
root.geometry('700x700')

# Stilizam textul si butoanele
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")

# Functie de crearerea Locului pentru text si crearea bazei de de cuvinte
def resetWritingLabels():
    # Lista de text cuvinte
    possibleTexts = [
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]
    # Alegem functia ce va pune cuvintele random
    text = random.choice(possibleTexts).lower()

    # definim unde textul se va desparti
    splitPoint = 0
    # aicea va fi sris textul deja scris de utilizator
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Aici se localizeaza textul care numai va fi scris de utilizator
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)
    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # Locul unde va scrie cat timp mai are utilizatorul
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Legarea si apelarea la funcții după o anumită perioadă de timp.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False

    # Calcularea cantității de cuvinte
    amountWords = len(labelLeft.cget('text').split(' '))

    # Distrugem toate widget-urile nedorite.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()
    # Afișați rezultatele testului cu un șir formatat
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Afisam butonul de a resetarta jocul
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    # Destrugem reultatul
    ResultLabel.destroy()
    ResultButton.destroy()

    # Repornim jocul
    resetWritingLabels()

def addSecond():
    # Adaugam inca un contor de cuvinte.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # Chemama aceasta functie fiecare secunda ca programul si utilizatorul sa nu intre in conflict(in timpul testului sunt pause in scris aceasta si este functia).
    if writeAble:
        root.after(1000, addSecond)

def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Stergerea din paretea dreapta.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Sterge din partea stanga.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #creaza un nou lable pentru urmatoarea litera
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass

# Aceastea functie proneste to testul
resetWritingLabels()

# Startam Tot programul si bibliotecile
root.mainloop()