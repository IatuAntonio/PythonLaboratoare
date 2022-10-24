def operatii(*arguments):
    my_list = []
    d = {}
    for arg in arguments:
        my_list.append(arg)
    for i in range(0, len(my_list)-1):
        d[f"{my_list[i]} & {my_list[i+1]}"] = set()
        d[f"{my_list[i]} | {my_list[i + 1]}"] = set()
        d[f"{my_list[i]} - {my_list[i + 1]}"] = set()
        d[f"{my_list[i + 1]} - {my_list[i]}"] = set()

    for i in range(0, len(my_list)-1):
        my_first_set = set(my_list[i])
        my_second_set = set(my_list[i+1])

        w = my_first_set.intersection(my_second_set)
        x = my_first_set.union(my_second_set)
        y = my_first_set - my_second_set
        z = my_second_set - my_first_set
        d[f"{my_list[i]} & {my_list[i+1]}"] = w
        d[f"{my_list[i]} | {my_list[i+1]}"] = x
        d[f"{my_list[i]} - {my_list[i+1]}"] = y
        d[f"{my_list[i+1]} - {my_list[i]}"] = z

    # for i in d.items():
    #     print(i)

    return d


def main():
    print(operatii({1, 2}, {2, 3}))


if __name__ == "__main__":
    main()
