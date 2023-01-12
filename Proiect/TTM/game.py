import sys
from tkinter import *
from PIL import Image, ImageTk
import random


def defineTraps():
    global mouse_position
    my_list = list(range(4, 9))
    random.seed()
    rnd = random.randrange(len(my_list))

    for i in range(0, my_list[rnd]):
        rnd_hex = random.randrange(120)
        if rnd_hex == mouse_position:
            rnd_hex = random.randrange(120)
        hexagon = coord[rnd_hex]
        canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                              hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                              fill="crimson", outline="darkviolet")

        coord[rnd_hex][-1] = "capcana"


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
    global mouse_position
    global you_lose
    global nr_player
    if difficulty != "player":
        for index in range(0, len(coord)):
            hexagon = coord[index]
            if verifyHexagon(event.x, event.y, hexagon) == 1 and mouse_position != index and hexagon[-1] != "capcana":
                coord[index][-1] = "capcana"
                canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0],
                                      hexagon[2][1],
                                      hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0],
                                      hexagon[5][1],
                                      fill="crimson", outline="darkviolet")
                print(index)
                moveMouse()
                ngh1 = myNeighbours(mouse_position)

                if you_lose == 1:
                    print("You lost")
                    sys.exit()

                if len(ngh1) != 6:
                    you_lose = 1
    else:
        if nr_player == 0:
            for index in range(0, len(coord)):
                hexagon = coord[index]
                if verifyHexagon(event.x, event.y, hexagon) == 1 and mouse_position != index and hexagon[
                    -1] != "capcana":
                    coord[index][-1] = "capcana"
                    canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0],
                                          hexagon[2][1],
                                          hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0],
                                          hexagon[5][1],
                                          fill="crimson", outline="darkviolet")
                    print(index)
                    # moveMouse()
                    nr_player = 1
                    ngh1 = myNeighbours(mouse_position)

                    if you_lose == 1:
                        print("You lost")
                        sys.exit()

                    if len(ngh1) != 6:
                        you_lose = 1
        else:
            ngh = myNeighboursValid(mouse_position)

            for index in range(0, len(ngh)):
                hexagon = coord[index]
                hexagon_mouse = coord[mouse_position]

                if verifyHexagon(event.x, event.y, hexagon) == 1 and mouse_position != index:
                    canvas.create_polygon(hexagon_mouse[0][0], hexagon_mouse[0][1], hexagon_mouse[1][0], hexagon_mouse[1][1], hexagon_mouse[2][0],
                                          hexagon_mouse[2][1],
                                          hexagon_mouse[3][0], hexagon_mouse[3][1], hexagon_mouse[4][0], hexagon_mouse[4][1], hexagon_mouse[5][0],
                                          hexagon_mouse[5][1],
                                          fill="darkorange", outline="darkviolet")
                    mouse_position = index
                    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW,
                                image=mouse)
                    nr_player = 0


def coordError(x1, x2):
    if x1 == x2 + 1 or x1 == x2 - 1 or x1 == x2:
        return True
    return False


def myNeighboursValid(position):
    neighbours = myNeighbours(position)
    valid_neighbours = list()

    for ngh in neighbours:
        if coord[ngh][-1] == "normal":
            valid_neighbours.append(ngh)

    return valid_neighbours


def myNeighbours(position):
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


def moveEasy():
    global mouse_position
    hexagon = coord[mouse_position]
    neighbours = myNeighboursValid(mouse_position)

    if len(neighbours) == 0:
        print("You win")
        sys.exit()

    canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                          hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                          fill="darkorange", outline="darkviolet")

    rnd = random.randrange(len(neighbours))
    mouse_position = neighbours[rnd]
    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW, image=mouse)


def moveMedium():
    global mouse_position
    global medium_rnd_go
    hexagon = coord[mouse_position]

    neighbours = myNeighboursValid(mouse_position)

    if len(neighbours) == 0:
        print("You win")
        sys.exit()

    if medium_rnd_go == 0:

        if mouse_position-2 in neighbours:
            mouse_position = mouse_position - 2
        else:
            rnd_rnd = random.randrange(0, 2)
            if len(neighbours) == 1:
                mouse_position = neighbours[0]
            else:
                mouse_position = neighbours[rnd_rnd]
    else:

        if mouse_position + 2 in neighbours:
            mouse_position = mouse_position + 2
        else:
            rnd_rnd = random.randrange(1, 3)
            if len(neighbours) == 1:
                mouse_position = neighbours[0]
            else:
                mouse_position = neighbours[rnd_rnd * (-1)]

    canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                          hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                          fill="darkorange", outline="darkviolet")

    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW, image=mouse)


def minimDistance(position):
    left = position
    cnt_left = 0

    while True:
        all_ngh = myNeighbours(left)

        if len(all_ngh) != 6:
            break

        ngh = myNeighboursValid(left)

        if left-2 in ngh:
            cnt_left = cnt_left + 1
            left = left - 2
        else:
            cnt_left = cnt_left + 1
            left = left - 2

    right = position
    cnt_right = 0

    while True:
        all_ngh = myNeighbours(right)

        if len(all_ngh) != 6:
            break

        ngh = myNeighboursValid(right)

        if right + 2 in ngh:
            cnt_right = cnt_right + 1
            right = right + 2
        else:
            cnt_right = cnt_right + 1
            right = right + 2

    up = position
    cnt_up = 0

    while True:
        all_ngh = myNeighbours(up)

        if len(all_ngh) != 6 or up < 22:
            break

        cnt_up = cnt_up + 2
        up = up - 22

    down = position
    cnt_down = 0

    while True:
        all_ngh = myNeighbours(down)

        if len(all_ngh) != 6 or down > 98:
            break

        cnt_down = cnt_down + 2
        down = down + 22

    minim = min([cnt_left, cnt_right, cnt_up, cnt_down])

    return minim


def isFinal(position , cnt):

    neighbours = myNeighboursValid(position)

    for ngh in neighbours:
        ngh_ngh = myNeighbours(ngh)
        if len(ngh_ngh) != 6:
            return 1
        if cnt >= 2:
            break
        else:
            valid_ngh = myNeighboursValid(ngh)
            cnt += 1
            for n in valid_ngh:
                if isFinal(n, cnt) == 1:
                    return 1

    return 0


def moveHard():
    global mouse_position

    hexagon = coord[mouse_position]

    neighbours = myNeighboursValid(mouse_position)

    if len(neighbours) == 0:
        print("You win")
        sys.exit()

    my_list = list()
    maxim = -1
    next_ngh = -1
    neighbours.reverse()
    for ngh in neighbours:

        all_neighbours = myNeighbours(ngh)
        if len(all_neighbours) != 6:
            next_ngh = ngh
            break
        scor = 0
        ngh_neighbours = myNeighboursValid(ngh)
        ngh_neighbours.remove(mouse_position)

        scor = len(ngh_neighbours)

        my_list.append((ngh, " ", scor))

        if isFinal(ngh, 0) == 1:
            next_ngh = ngh
            scor = 10

        if scor > maxim:
            maxim = scor
            next_ngh = ngh


    # print(mouse_position)

    mouse_position = next_ngh

    # print(my_list)

    canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                          hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                          fill="darkorange", outline="darkviolet")

    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW, image=mouse)


def moveMouse():

    if difficulty == "easy":
        moveEasy()
    if difficulty == "medium":
        moveMedium()
    if difficulty == "hard":
        moveHard()


def testDifficulty():
    global difficulty
    file = open("dificulate.txt", "r")
    difficulty = file.read()


board = Tk()

board.title("TRAP THE MOUSE")

board.geometry("1120x850")

canvas = Canvas(board, width=1120, height=850, bg="lightseagreen")

canvas.bind("<Button-1>", pressButton)

canvas.pack(padx=10, pady=10) # deseneaza pe board

coord = list()

you_lose = 0

difficulty = "non"

nr_player = 0

medium_rnd_go = random.randrange(0, 2)

testDifficulty()

print(difficulty)

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

defineTraps()
print(myNeighbours(83))

board.mainloop()
