def fnc(pairs):
    my_list = []

    for pair in pairs:
        # print(pair)
        d = dict()
        d["sum"] = pair[0] + pair[1]
        d["prod"] = pair[0] * pair[1]
        d["pow"] = pair[0] ** pair[1]
        my_list.append(d)

    print(my_list)
    return my_list


def main():
    fnc(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)])


if __name__ == "__main__":
    main()
