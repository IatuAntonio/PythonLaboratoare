from tkinter import *

board = Tk()

board.title("Trap The Mouse")

board.geometry("1120x850")

canvas = Canvas(board, width=1120, height=850, bg="saddlebrown")

canvas.pack(padx=10, pady=10)

canvas.create_text(560, 200, text="Trap The Mouse", fill="darkorange", font=("Brush Script MT", 60))

Button(canvas, text="Start Game", width=40, height=2, command=None, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=300)
Button(canvas, text="Option", width=40, height=2, command=None, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=450)
Button(canvas, text="Quit Game", width=40, height=2, command=None, bg="crimson", font=("Brush Script MT", 17)).place(x=340, y=600)


board.mainloop()
