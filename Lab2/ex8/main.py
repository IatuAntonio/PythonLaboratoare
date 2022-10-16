def ascii_test(my_list, flag=True, x=1):
    new_list = []
    for i in my_list:
        nl = []
        for j in i:
            # print(f"{j} --- {ord(j)} --- {flag}")
            if flag is False and ord(j) % x != 0:
                nl.append(j)
            if flag is True and ord(j) % x == 0:
                nl.append(j)
        if len(nl) > 0:
            new_list.append(nl)
    return new_list


def main():
    x = 1
    try:
        x = int(input("x = "))
    except ValueError:
        print("X nu est e numar")

    my_list = input("Your list:\n")
    my_list = my_list.split(" ")
    flag = True
    try:
        txt = input("flag = ")
        if txt == "False":
            flag = False
        elif txt == "True":
            flag = True
    except ValueError:
        print("Flag nu este bolean")

    print(ascii_test(my_list, flag, x))


if __name__ == "__main__":
    main()
