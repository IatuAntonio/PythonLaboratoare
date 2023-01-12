


import sys
from tkinter import *




def startGame():
    import game


def gameEasy():
    file = open("dificulate.txt", "w")
    file.write("easy")
    file.close()
    board.destroy()
    startGame()


def gameMedium():
    file = open("dificulate.txt", "w")
    file.write("medium")
    file.close()
    board.destroy()
    startGame()


def gameHard():
    file = open("dificulate.txt", "w")
    file.write("hard")
    file.close()
    board.destroy()
    startGame()


def gamePlayer():
    file = open("dificulate.txt", "w")
    file.write("player")
    file.close()
    board.destroy()
    startGame()


def quitGame():
    sys.exit()


def goInterface():
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


board = Tk()

width = 1120  # Width
height = 850  # Height

screen_width = board.winfo_screenwidth()  # Width of the screen
screen_height = board.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

board.geometry('%dx%d+%d+%d' % (width, height, x, y))

board.title("Trap The Mouse")

board.geometry("1120x850")

canvas = Canvas(board, width=1120, height=850, bg="saddlebrown")

canvas.pack(padx=10, pady=10)

canvas.create_text(560, 200, text="Trap The Mouse", fill="darkorange", font=("Brush Script MT", 60))

Button(canvas, text="Start Game", width=40, height=2, command=goInterface, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=300)
Button(canvas, text="Option", width=40, height=2, command=None, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=450)
Button(canvas, text="Quit Game", width=40, height=2, command=quitGame, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=600)


board.mainloop()
