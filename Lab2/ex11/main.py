def ord_tuples(*arguments):
    my_list = []
    for arg in arguments:
        my_list.append(list(arg))
    n = len(my_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if my_list[j][1][2] > my_list[j+1][1][2]:
                aux = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = aux

    return my_list


def main():
    print(ord_tuples(("abc", "bcd"), ("abc", "zza"), ("bda", "acb")))


if __name__ == "__main__":
    main()
