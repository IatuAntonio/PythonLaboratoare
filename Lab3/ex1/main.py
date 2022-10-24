def operatii(first_list, second_list):
    my_first_set = set(first_list)
    my_second_set = set(second_list)
    # my_first_set = first_list
    # my_second_set = second_list

    w = my_first_set.intersection(my_second_set)
    x = my_first_set.union(my_second_set)
    y = my_first_set - my_second_set
    z = my_second_set - my_first_set

    return w, x, y, z


def main():
    print(operatii([1, 2, 3, 4, 5], [3, 4, 5, 5, 6, 7, 8]))


if __name__ == "__main__" :
    main()
