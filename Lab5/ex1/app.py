import utils


def main():

    while 1:
        text = input()
        if text == "q":
            break
        nr = 0
        try:
            nr = int(text)
            print(f"Cel mai mic nr prim mai mare ca {nr} este {utils.process_item(nr)}")
        except ValueError:
            print("Nu este numar")


if __name__ == "__main__":
    main()
