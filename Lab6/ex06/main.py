import re


def my_fnc(text):
    new_list = []
    new_list = text.split(" ")
    my_list = []
    censured = []

    for element in new_list:
        ceva = re.findall(r"^(a|e|i|o|u)\w*(a|e|i|o|u)$", element)
        if len(ceva) != 0:
            my_list.append(ceva)
            cns = '*' * len(element)
            censured.append(cns)
        elif len(ceva) == 0:
            censured.append(element)

    txt = " ".join(censured)

    print(txt)

    return txt


def main():
    my_fnc("ana are mere ce mai vrei undeva aurelee ce ai facut")


if __name__ == "__main__":
    main()