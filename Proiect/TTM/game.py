from tkinter import *
from PIL import Image, ImageTk



board = Tk()

board.title("TRAP THE MOUSE")

board.geometry("1280x850")

canvas = Canvas(board, width=1280, height=850, bg="lightseagreen")

# canvas.bind("<Button-1>", PressButton)

canvas.pack(padx=10, pady=10) # deseneaza pe board

# canvas.create_polygon(67, 13, 110, 35, 110, 78, 67, 100, 23, 78, 23, 35, fill="darkorange", outline="darkviolet")

coord = list()

for line in range(0, 6):
    for row in range(0, 11):

        canvas.create_polygon(67 + (row * 91), 13 + (line * 134), 112 + (row * 91), 36 + (line * 134), 112 + (row * 91),
                              80 + (line * 134), 67 + (row * 91), 103 + (line * 134),
                              22 + (row * 91), 80 + (line * 134), 22 + (row * 91), 36 + (line * 134), fill="darkorange",
                              outline="darkviolet")

        coord.append([[67 + (row * 91), 13 + (line * 134)], [112 + (row * 91), 36 + (line * 134)],
                      [112 + (row * 91), 80 + (line * 134)], [67 + (row * 91), 103 + (line * 134)],
                      [22 + (row * 91), 80 + (line * 134)], [22 + (row * 91), 36 + (line * 134)], ["normal"]])

        if line != 5:
            canvas.create_polygon(112 + (row * 91), 80 + (line * 134), 157 + (row * 91), 103 + (line * 134), 157 + (row * 91),
                              147 + (line * 134), 112 + (row * 91), 170 + (line * 134),
                              67 + (row * 91), 147 + (line * 134), 67 + (row * 91), 103 + (line * 134), fill="darkorange",
                              outline="darkviolet")
            coord.append([[112 + (row * 91), 80 + (line * 134)], [157 + (row * 91), 103 + (line * 134)],
                         [157 + (row * 91), 147 + (line * 134)], [112 + (row * 91), 170 + (line * 134)],
                         [67 + (row * 91), 147 + (line * 134)], [67 + (row * 91), 103 + (line * 134)], ["normal"]])




board.mainloop()
