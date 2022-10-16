from colorama import Fore


def my_song(musical_notes, moves, start):
    new_order = [musical_notes[start]]
    for i in moves:
        start += i
        if start > len(musical_notes):
            start -= len(musical_notes)
        if start < 0:
            start = len(musical_notes) + start
        new_order.append(musical_notes[start])

    return new_order


def main():
    musical_notes = input("Your musical notes:\n")
    musical_notes = musical_notes.split(" ")
    txt = input("Moves:\n")
    my_list = txt.split(" ")
    moves = []
    try:
        for i in my_list:
            moves.append(int(i))
    except ValueError:
        print(f"{Fore.RED}Miscarile introduse nu sunt numere!!!")
        return 0
    nr = input("Start point:\n")
    try:
        nr = int(nr)
    except ValueError:
        print(f"{Fore.RED}Start point nu este numar!!!")

    print(my_song(musical_notes, moves, nr))


if __name__ == "__main__":
    main()