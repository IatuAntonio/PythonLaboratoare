import re


def my_function(txt_reg, text, number):
    txt_reg += f'{{{number}}}'
    print(txt_reg)
    my_list = re.findall(txt_reg, text)
    print(my_list)


def main():
    my_function(r"\w", "ana 345 fdf f sd 342 fsd 934", 3)


if __name__ == "__main__":
    main()
