import re


def my_split(text):
    my_list = re.findall(r"\w+", text)
    print(my_list)


def main():
    my_split("ana are mere asdas ads++++ asd.dsa., jj42!!!3nn23 , *1///1ds")


if __name__ == "__main__":
    main()
