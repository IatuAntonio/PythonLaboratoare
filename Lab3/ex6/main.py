def unique_duplicates(my_list):
    my_set = set()
    my_set.update(my_list)
    ms1 = set()
    # print(my_set)
    for element in my_set:
        if element in my_list:
            my_list.remove(element)
            if element not in my_list:
                ms1.add(element)

    my_set = set()
    my_set.update(my_list)
    # print(ms1)
    # print(my_set)
    my_tuple = (len(ms1), len(my_set))
    return my_tuple


def main():
    print(unique_duplicates([1, 3, 4, 1, 3, 4, 1, 1, 2, 5, 6, 7, 7, 8, 1, 11]))


if __name__ == "__main__":
    main()
