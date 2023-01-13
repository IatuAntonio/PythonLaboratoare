"""
Fisierul game.py este cel ce contine jocul propriu-zis. Programul testeaza ce este in fisierul dificultate si pe baza
rezultatului respectiv isi va schimba comportamentul. Jocul are 4 moduri de a fi jucat acestea fiind easy, medium, hard
si player vs player, fiecare avand un algoritm diferit in spate.
"""


import sys
from tkinter import *
from PIL import Image, ImageTk
import random


def forWin(text):
    """Distrug canvasul curent pentru a crea unul nou in care voi scrie continutul variabile text

    :param text: Este mesajul ce va fi afisat in canvasul nou creat (ex: "You Win" or "You Lost")

    :return:
    """
    canvas.destroy()
    win_game = Canvas(board, width=1120, height=850, bg="saddlebrown")
    win_game.pack(padx=10, pady=10)
    win_game.create_text(560, 100, text=text, fill="darkorange", font=("Brush Script MT", 60))


def defineTraps():
    """Definesc unde vor fi plasate capcanele de la inceputul jocului
    In my_list avem numaru de capcane afisate la deschiderea jocului. Cu ajutorul lui rnd vom alege o valoare aleatorie
     din lista pentru a da mereu un numar diferit de capcane. In for vom alege un hexagon (diferit de pozitia initiala
     a soarecelui) pe care il vom colora in culoarea crimson aratand astfel faptul ca este o capcana. La final in vectorul
     coord care contine coordonatele tuturor hexagoanelor vom preciza ca hexagonul nu mai este normal ci a devenit o
     capcana
    :return:
    """
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
    """Calculeaza aria triunghiului

    :param x1:  Coordonata x pentru primul punct
    :param y1:  Coordonata y pentru primul punct
    :param x2:  Coordonata x pentru al doilea punct
    :param y2:  Coordonata y pentru al doilea punct
    :param x3:  Coordonata x pentru al treilea punct
    :param y3:  Coordonata y pentru al treilea punct
    :return:
    """
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def pointInTheTriangle(x1, y1, x2, y2, x3, y3, x, y):
    """Testam daca un punct se afla in interiorul unui triunghi

    :param x1: Coordonata x pentru primul punct al triunghiului
    :param y1: Coordonata y pentru primul punct al triunghiului
    :param x2: Coordonata x pentru al doilea punct al triunghiului
    :param y2: Coordonata y pentru al doilea punct al triunghiului
    :param x3: Coordonata x pentru al treilea punct al triunghiului
    :param y3: Coordonata y pentru al treilea punct al triunghiului
    :param x: Coordonata x a puntului testat
    :param y: Coordonata y a puntului testat
    :return: True - daca apartine, False - daca nu apartine
    """
    a = float(trArea(x1, y1, x2, y2, x3, y3))
    a1 = float(trArea(x, y, x2, y2, x3, y3))
    a2 = float(trArea(x1, y1, x, y, x3, y3))
    a3 = float(trArea(x1, y1, x2, y2, x, y))
    return bool(a == a1 + a2 + a3)


def verifyHexagon(x, y, hexagon):
    """Testam daca punctul oferit apartine hexagonului

    Impartim hexagonul intr-un dreptungi si 2 triunghiuri si verificam daca apartin acestora

    :param x: Coordonata x a punctului
    :param y: Coordonata y a punctului
    :param hexagon: o lista de liste ce contin coordonatele colturilor hexagonului
    :return: 1 - apartine hexagonului, 0 - nu apartine hexagonului
    """
    if hexagon[4][0] <= x <= hexagon[2][0] and hexagon[1][1] <= y <= hexagon[4][1]:
        return 1

    if pointInTheTriangle(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[5][0], hexagon[5][1], x, y):
        return 1

    if pointInTheTriangle(hexagon[2][0], hexagon[2][1], hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], x, y):
        return 1

    return 0


def pressButton(event):
    """Adaug o capcana pe tabla

    Pentru modurile de joc easy, medium si hard functia are acelasi comportament: parcurg toate hexagoanele si testez pentru
    fiecare daca a fost cumva apasat. In cazul in care hexagonul a fost apasat si acesta este unul normal si este diferit de pozitia
    curenta a soarecelui atunci il voi transforma intr-o capcana, schimbandu-i culoarea si tipul. Totodata aceasta functie
    este cea care anunta daca jucatorul a pierdut acest lucru realizandu-se cand pozitia in care se afla soarecele nu mai
    are 6 vecini.
    Pentru modul de player vs player se va realiza relatic la fel doar ca se vor lua doua cazuri pe baza variabilei nr_player.
    Pentru valoarea 0 va muta playerul ca in mod normal ca si la celelalte moduri, iar pentru valoarea 1 in loc sa adaugam
    o capcana vom muta soarecele pe o pozitie vecina valabila

    :param event: Paramentrul din care se iau coordonatele punctului care a fost apasat
    :return:
    """
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
                moveMouse()
                ngh1 = myNeighbours(mouse_position)

                if you_lose == 1:
                    forWin("You lost")

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
                    # print(index)
                    # moveMouse()
                    nr_player = 1
                    ngh1 = myNeighboursValid(mouse_position)

                    if len(ngh1) == 0:
                        forWin("Player Win")
                        # print("PLAYER WIN")
                        # sys.exit()
        else:
            ngh = myNeighboursValid(mouse_position)

            for index in range(0, len(ngh)):
                vecin = ngh[index]
                hexagon = coord[vecin]
                hexagon_mouse = coord[mouse_position]

                if verifyHexagon(event.x, event.y, hexagon) == 1 and mouse_position != vecin:

                    canvas.create_polygon(hexagon_mouse[0][0], hexagon_mouse[0][1], hexagon_mouse[1][0], hexagon_mouse[1][1], hexagon_mouse[2][0],
                                          hexagon_mouse[2][1],
                                          hexagon_mouse[3][0], hexagon_mouse[3][1], hexagon_mouse[4][0], hexagon_mouse[4][1], hexagon_mouse[5][0],
                                          hexagon_mouse[5][1],
                                          fill="darkorange", outline="darkviolet")
                    mouse_position = vecin
                    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW,
                                image=mouse)
                    nr_player = 0
                    if len(myNeighbours(mouse_position)) != 6:
                        forWin("Mouse Win")


def coordError(coord1, coord2):
    """Distanta dintre hexagoane diferita

    Unele hexagoane create nu isi unesc laturile destul de bine fiind o mica distanta intre acestea. Petru a gasi vecinii
    intr-un mod cat mai corect am luat o marja de eroare pentru ca diferenta respectiva dintre laturi sa nu influenteze rezultatul.
    Din reprezentare am observat ca marja de eroare este de 1 px.

    :param coord1: Coordonata primului punct
    :param coord2: Coordonata celui de al doilea punct
    :return: True - daca marja de eroare este potrivita, False - punctele nu sunt chiar vecine
    """
    if coord1 == coord2 + 1 or coord1 == coord2 - 1 or coord1 == coord2:
        return True
    return False


def myNeighboursValid(position):
    """Calculam vecinii normali (care nu sunt capcane)

    :param position: poziti soarecelui in momentul curent
    :return: returnam vecinii care nu sunt capcane
    """
    neighbours = myNeighbours(position)
    valid_neighbours = list()

    for ngh in neighbours:
        if coord[ngh][-1] == "normal":
            valid_neighbours.append(ngh)

    return valid_neighbours


def myNeighbours(position):
    """Calculam vecinii hexagonului curent

    Pe baza celor 3 colcuti precizate mai jos (0, 2, 4) vom putea calcula care sunt hexagoanele vecine cu pozitia curenta.
    Vom lua initial coordonatele celor 3 colturi, apoi vom parcurge toate hexagoanele testand daca colturile 0, 2, 4
    sunt aceleasi (cu marja de eroare) cu ale hexagonului initial. In cazul in care sunt indeplinite conditiile hexagonul
    respectiv va fi introdus in lista de vecini

    :param position: pozitia pe care se afla soarece in momentul actual
    :return: o lista cu toti vecinii
    """
    mouse_x0 = coord[position][0][0]
    mouse_y0 = coord[position][0][1]

    mouse_x2 = coord[position][2][0]
    mouse_y2 = coord[position][2][1]

    mouse_x4 = coord[position][4][0]
    mouse_y4 = coord[position][4][1]

    neighbours = list()

    for index in range(0, len(coord)):
        hexagon = coord[index]

        hexagonx0 = hexagon[0][0]
        hexagony0 = hexagon[0][1]

        hexagonx2 = hexagon[2][0]
        hexagony2 = hexagon[2][1]

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
    """Mergem random pe un vecin

    Calculam care este pozitia curenta a soarecelui si vecinii valizi a aceste pozitii. Vom sterge soarecele de pe pozitia
    curenta, actualizand pozitia soarecelui cu a unuia dintre vecinii valizi ai sai. In cazul in care soarecele nu mai are
    niciun vecin valid inseamna ca nu mai are unda sa se duca, deci, prin urmare userul va castiga.

    :return: In cazul in care userul castiga functia va returna 0
    """
    global mouse_position
    hexagon = coord[mouse_position]
    neighbours = myNeighboursValid(mouse_position)

    if len(neighbours) == 0:
        forWin("You Win")
        return 0

    canvas.create_polygon(hexagon[0][0], hexagon[0][1], hexagon[1][0], hexagon[1][1], hexagon[2][0], hexagon[2][1],
                          hexagon[3][0], hexagon[3][1], hexagon[4][0], hexagon[4][1], hexagon[5][0], hexagon[5][1],
                          fill="darkorange", outline="darkviolet")

    rnd = random.randrange(len(neighbours))
    mouse_position = neighbours[rnd]
    canvas.create_image(coord[mouse_position][5][0] + 18, coord[mouse_position][5][1] - 3, anchor=NW, image=mouse)


def moveMedium():
    """Alegem random stanga sau dreapta si incercam sa ajungem la capete

    Pentru pozitia actuala a soarecelui vom calcula vecinii valizi. In funtie de variabila medium_rnd_go soarecele se
    va deplasa la stanga sau la dreapta. In cazul in care vecinul din dreapta/stanga este un hexagon normal ne vom muta
    pe el (testam hexagonul la distanta de 2 fata de noi deoarece pe linii hexagoanele sunt ori pare ori impare vecinii
    lui 45 spre exemplu fiind 43 si 47), insa, daca vecinul respectiv este o capcana vom alege sa mergem random pe unul
    dintre primii doi vecini.

    :return: In cazul in care userul castiga functia va returna 0
    """
    global mouse_position
    global medium_rnd_go
    hexagon = coord[mouse_position]

    neighbours = myNeighboursValid(mouse_position)

    if len(neighbours) == 0:
        forWin("You Win")
        return 0

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
        forWin("You Win")
        return 0
        # print("You win")
        # sys.exit()

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


    mouse_position = next_ngh

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

width = 1120
height = 850

screen_width = board.winfo_screenwidth()
screen_height = board.winfo_screenheight()

x_screen = (screen_width / 2) - (width / 2)
y_screen = (screen_height / 2) - (height / 2)

board.geometry('%dx%d+%d+%d' % (width, height, x_screen, y_screen))

canvas = Canvas(board, width=1120, height=850, bg="saddlebrown")

canvas.bind("<Button-1>", pressButton)

canvas.pack(padx=10, pady=10) # deseneaza pe board

coord = list()

you_lose = 0

difficulty = "non"

nr_player = 0

medium_rnd_go = random.randrange(0, 2)

testDifficulty()

# print(difficulty)

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
# print(myNeighbours(83))

board.mainloop()
