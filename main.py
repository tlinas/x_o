from tkinter import *
from Tikrinimas import tikrinimas
import random
from Do_or_die import do_or_die

window = Tk()
window.geometry("500x250")
main = Frame(window)
main.pack()
radio_button = IntVar()
mygtukas = []
player = "O"
pradeda = False

class Mygtukas():
    def __init__(self,eilutes_remas,b):
        self.position = len(mygtukas)
        mygtukas.append(Button(eilutes_remas, text=b, relief=GROOVE, width=2, command=lambda: self.darytiejima()))
        mygtukas[self.position].pack(side="left")

    def darytiejima(self):
        ejimas(self.position)

def pagrindinis_langas():
    antraste1 = Label(main, text="Kryziuku - nuliuku zaidimas")
    R1 = Radiobutton(main, text="Pradeda zmogus", variable=radio_button, value=1, command=antras)
    R2 = Radiobutton(main, text="Pradeda kompiuteris", variable=radio_button, value=2, command=pirmas)
    paleidimas = Button(main, text="Pradedam", command=paleisti)
    pabaiga = Button(main, text="Pabaiga", command=iseiti)

    antraste1.pack(side=TOP)
    R1.pack(side=TOP, anchor=W)
    R2.pack(side=TOP, anchor=W)
    paleidimas.pack(fill=X)
    pabaiga.pack(fill=Y)

def paleisti():
    widget_list = all_children(main)
    for item in widget_list:
        item.destroy()
    pagrindinis_langas()
    global mygtukas
    global lentele
    global player
    mygtukas = []
    lentele = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "O"
    piesti_lentele()
    if pradeda:
        player = "X"
        randomizatorius(lentele, player)


def piesti_lentele():
    for i, b in enumerate(lentele):
        if i % 3 == 0:
            eilutes_remas = Frame(main)
            eilutes_remas.pack(side="top")
        Mygtukas(eilutes_remas,b)

def UpdateBoard(positionClicked):
    global player
    for i, b in enumerate(lentele):
        mygtukas[i].config(text=b)
    mygtukas[positionClicked].configure(state=DISABLED)
    if tikrinimas(lentele) == "X":        # funkcija is Tikrinimas modulio, tikrina ar kas nors laimejo zaidima
        pergale()
        uzsaldyti()
    elif tikrinimas(lentele) == "O":
        pergale()
        uzsaldyti()
    elif sum(type(c) is str for c in lentele if c != " ") == 9:
        laimetojas = Label(main, text=f'Lygiosios')
        laimetojas.pack(side=BOTTOM)


def uzsaldyti(): #
    for i, b in enumerate(lentele):
        mygtukas[i].configure(state=DISABLED)

def ejimas(positionClicked):
    global player
    if player == "O":
        lentele[positionClicked] = "X"
        player = "X"
    else:
        lentele[positionClicked] = "O"
        player = "O"
    UpdateBoard(positionClicked)
    if player == "O":
        player = "X"
    else:
        player = "O"
        UpdateBoard(positionClicked)
    if sum(type(c) is str for c in lentele if c != " ") < 9:
        position = do_or_die(lentele)
        if position is not None:
            lentele[position] = player
            UpdateBoard(position)
        else:
            randomizatorius(lentele, player)


def randomizatorius(lentele, player):
    index = [i for i, x in enumerate(lentele) if x == " "]
    start = [1, 3, 5, 7]
    avail = sorted(set(index) - set(start))
    if [i for i in avail if i == 4]:
        choice = 4
        lentele[choice] = player
        UpdateBoard(choice)
    else:
        try:
            choice = random.choice(avail)
            lentele[choice] = player
            UpdateBoard(choice)
        except:
            choice = do_or_die(lentele)
            if choice is not None:
                lentele[int(choice)] = player
                UpdateBoard(choice)
            else:
                choice = random.choice(index)
                lentele[int(choice)] = player
                UpdateBoard(choice)


def pirmas():
    global pradeda
    pradeda = True

def antras():
    global pradeda
    pradeda = False

def iseiti():
    window.withdraw()
    sys.exit()

def all_children (main):
    _list = main.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list

def pergale():
    laimetojas = Label(main, text=f'Laimejo, {tikrinimas(lentele)}')
    laimetojas.pack(side=BOTTOM)

pagrindinis_langas()
main.mainloop()
