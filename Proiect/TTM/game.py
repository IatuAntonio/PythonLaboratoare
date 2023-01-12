from tkinter import *
from PIL import Image, ImageTk

# aria triunghi
def trArea(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def pointInTheTriangle(x1, y1, x2, y2, x3, y3, x, y):
    a = float(trArea(x1, y1, x2, y2, x3, y3))
    a1 = float(trArea(x, y, x2, y2, x3, y3))
    a2 = float(trArea(x1, y1, x, y, x3, y3))
    a3 = float(trArea(x1, y1, x2, y2, x, y))
    return a == a1 + a2 + a3


def verifyHexagon(x, y, hexagon):
    if hexagon[4][0] <= x <= hexagon[2][0] and hexagon[1][1] <= y <= hexagon[4][1]:
        return 1

    if pointInTheTriangle(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[5][0], hexagon[5][1], x, y):
        return 1

    if pointInTheTriangle(hexagon[2][0], hexagon[2][1], hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], x, y):
        return 1

    return 0


def pressButton(event):

    for index in range (0, len(coord)):
        hexagon = coord[index]
        if verifyHexagon(event.x, event.y, hexagon) == 1 and mouse_position != index and hexagon[-1] != "capcana":
            coord[index][-1] = "capcana"
            print(index)
            canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                                  hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                                  fill="crimson", outline="darkviolet")


def coordError(x1, x2):
    if x1 == x2 + 1 or x1 == x2 - 1 or x1 == x2:
        return True
    return False


def my_neighbours(position):
    mouse_x0 = coord[position][0][0]
    mouse_y0 = coord[position][0][1]

    mouse_x2 = coord[position][2][0]
    mouse_y2 = coord[position][2][1]

    mouse_x4 = coord[position][4][0]
    mouse_y4 = coord[position][4][1]

    neighbours = list()

    for index in range(0, len(coord)):
        hexagon = coord[index]

        hexagonx2 = hexagon[2][0]
        hexagony2 = hexagon[2][1]

        hexagonx0 = hexagon[0][0]
        hexagony0 = hexagon[0][1]

        hexagonx4 = hexagon[4][0]
        hexagony4 = hexagon[4][1]

        if coordError(hexagonx2, mouse_x4) and coordError(hexagony2, mouse_y4):
            neighbours.append(index)

        if coordError(hexagonx0, mouse_x4) and coordError(hexagony0, mouse_y4):
            neighbours.append(index)

        if coordError(hexagonx0, mouse_x2) and coordError(hexagony0, mouse_y2):
            neighbours.append(index)

        if coordError(hexagonx4, mouse_x2) and coordError(hexagony4, mouse_y2):
            neighbours.append(index)

        if coordError(hexagonx2, mouse_x0) and coordError(hexagony2, mouse_y0):
            neighbours.append(index)

        if coordError(hexagonx4, mouse_x0) and coordError(hexagony4, mouse_y0):
            neighbours.append(index)



    return neighbours


board = Tk()

board.title("TRAP THE MOUSE")

board.geometry("1120x850")

canvas = Canvas(board, width=1120, height=850, bg="lightseagreen")

canvas.bind("<Button-1>", pressButton)

canvas.pack(padx=10, pady=10) # deseneaza pe board

coord = list()

for line in range(0, 6):
    for row in range(0, 11):

        canvas.create_polygon(67 + (row * 91), 13 + (line * 134), 112 + (row * 91), 36 + (line * 134), 112 + (row * 91),
                              80 + (line * 134), 67 + (row * 91), 103 + (line * 134),
                              22 + (row * 91), 80 + (line * 134), 22 + (row * 91), 36 + (line * 134), fill="darkorange",
                              outline="darkviolet")

        coord.append([[67 + (row * 91), 13 + (line * 134)], [112 + (row * 91), 36 + (line * 134)],
                      [112 + (row * 91), 80 + (line * 134)], [67 + (row * 91), 103 + (line * 134)],
                      [22 + (row * 91), 80 + (line * 134)], [22 + (row * 91), 36 + (line * 134)], "normal"])

        if line != 5:
            canvas.create_polygon(112 + (row * 91), 80 + (line * 134), 157 + (row * 91), 103 + (line * 134), 157 + (row * 91),
                              147 + (line * 134), 112 + (row * 91), 170 + (line * 134),
                              67 + (row * 91), 147 + (line * 134), 67 + (row * 91), 103 + (line * 134), fill="darkorange",
                              outline="darkviolet")
            coord.append([[112 + (row * 91), 80 + (line * 134)], [157 + (row * 91), 103 + (line * 134)],
                         [157 + (row * 91), 147 + (line * 134)], [112 + (row * 91), 170 + (line * 134)],
                         [67 + (row * 91), 147 + (line * 134)], [67 + (row * 91), 103 + (line * 134)], "normal"])

mouse = ImageTk.PhotoImage(Image.open("mrsmouse.png"))

mouse_position = 55

canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW, image=mouse)

print(my_neighbours(mouse_position))


board.mainloop()
