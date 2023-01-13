"""
Main.py este cel care se ocupa cu parea de inceput a jocului. In acest modul se crea primul canvas in care se vor afisa
titlul si butoanele. Din acest meniu se poate avansa intr-un nou canvas in care vom regasi cele 4 moduri de joc (Easy,
Medium, Hard, Player vs Player) sau se poate in inchide jocul prin apasarea butonului de quit. Canvsul care va avea butoanele
ce permit alegerea modului de joc va lega main.py de game.py permitand astfel ca jocul propriu-zis sa ruleze
"""


import sys
from tkinter import *


def startGame():
    """ Apelam continutul lui game.py
    :return:
    """
    import game


def gameEasy():
    """Modificam modul de joc
    Functia va deschide fisierul dificultate.txt pentru a scrie ce dificultate am ales pentru jocul nostru. Acest fisier
    este partajat cu game.py, acesta verificand cu ajutorul fisierului ce modalitate va folosi (in cazul nostru fiind easy)
    :return:
    """
    file = open("dificulate.txt", "w")
    file.write("easy")
    file.close()
    board.destroy()
    startGame()


def gameMedium():
    """Modificam modul de joc
    Functia va deschide fisierul dificultate.txt pentru a scrie ce dificultate am ales pentru jocul nostru. Acest fisier
    este partajat cu game.py, acesta verificand cu ajutorul fisierului ce modalitate va folosi (in cazul nostru fiind medium)
    :return:
    """
    file = open("dificulate.txt", "w")
    file.write("medium")
    file.close()
    board.destroy()
    startGame()


def gameHard():
    """Modificam modul de joc
    Functia va deschide fisierul dificultate.txt pentru a scrie ce dificultate am ales pentru jocul nostru. Acest fisier
    este partajat cu game.py, acesta verificand cu ajutorul fisierului ce modalitate va folosi (in cazul nostru fiind hard)
    :return:
    """
    file = open("dificulate.txt", "w")
    file.write("hard")
    file.close()
    board.destroy()
    startGame()


def gamePlayer():
    """Modificam modul de joc
    Functia va deschide fisierul dificultate.txt pentru a scrie ce dificultate am ales pentru jocul nostru. Acest fisier
    este partajat cu game.py, acesta verificand cu ajutorul fisierului ce modalitate va folosi (in cazul nostru fiind player)
    :return:
    """
    file = open("dificulate.txt", "w")
    file.write("player")
    file.close()
    board.destroy()
    startGame()


def quitGame():
    """Functia este folosita pentru butonul Quit facand ca programul sa se opreasca

    :return:
    """
    sys.exit()


def goInterface():
    """Mutam la interfata din care alegem modul de joc

        Pentru a crea noua interfata vom avea nevoie sa distrugem vechea interfata. Vom face pe urma un nou canvas (choose_game)
        in care vom crea 4 butoane ce vor fi aferente modurilor de joc. Fiecarui buton i se va atribui o functie (din cele ilustrate
        mai sus) care ii va permite sa deschida jocul in modul in care doreste

    :return:
    """
    global canvas
    canvas.destroy()
    choose_game = Canvas(board, width=1120, height=850, bg="saddlebrown")
    choose_game.pack(padx=10, pady=10)

    choose_game.create_text(560, 100, text="Choose how to play", fill="darkorange", font=("Brush Script MT", 60))

    Button(choose_game, text="Easy", width=40, height=2, command=gameEasy, bg="crimson",
           font=("Brush Script MT", 17)).place(x=340, y=200)
    Button(choose_game, text="Medium", width=40, height=2, command=gameMedium, bg="crimson", font=("Brush Script MT", 17)).place(
        x=340, y=350)
    Button(choose_game, text="Hard", width=40, height=2, command=gameHard, bg="crimson",
           font=("Brush Script MT", 17)).place(x=340, y=500)
    Button(choose_game, text="Player vs Player", width=40, height=2, command=gamePlayer, bg="crimson",
           font=("Brush Script MT", 17)).place(x=340, y=650)


"""
    Mai jos am ilustrat  cum se va creea tabla (board) pe care vom desena canvasul nostru.
    Dupa initializare vom face astfel incat board sa fie afisat in centrul ecranului pentru a fi o experienta mai placuta.
    Pe urma voi initializa si canvasul pentru a introduce titlul jocului si butoanele din meniul principal
    
"""

board = Tk()

width = 1120  # Width
height = 850  # Height

screen_width = board.winfo_screenwidth()  # Width of the screen
screen_height = board.winfo_screenheight()  # Height of the screen

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

board.geometry('%dx%d+%d+%d' % (width, height, x, y))

board.title("Trap The Mouse")

canvas = Canvas(board, width=1120, height=850, bg="saddlebrown")

canvas.pack(padx=10, pady=10)

canvas.create_text(560, 200, text="Trap The Mouse", fill="darkorange", font=("Brush Script MT", 60))

Button(canvas, text="Start Game", width=40, height=2, command=goInterface, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=300)
Button(canvas, text="Option", width=40, height=2, command=None, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=450)
Button(canvas, text="Quit Game", width=40, height=2, command=quitGame, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=600)

board.mainloop()
