import re


def my_fnc(text, reg_text):
    my_list = []
    for element in text:
        ceva = re.findall(reg_text, element)
        my_list.append(ceva)

    print(my_list)


def main():
    my_list = ["ana 55", "dsad 787 dasffg 987", "gdysagud fdfds   fsd f sd ", "4565 534 fdgfd"]
    my_fnc(my_list, r"[0-9]{3}")


if __name__ == "__main__":
    main()
