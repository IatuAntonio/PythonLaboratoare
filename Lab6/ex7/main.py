import re


def my_fnc(cnp):
    if re.match(r"[1-8][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|[1-4][0-8])([0-9][0-9][0-9])[0-9]", cnp):
        print("da")
    else:
        print("nu")


def main():
    my_fnc("9010850671385")
    my_fnc("5010804071385")


if __name__ == "__main__":
    main()