def rhyme_group(*arguments):
    dictionary = {}
    my_list = []
    for arg in arguments:
        for elm in arg:
            dictionary[elm[-2] + elm[-1]] = ""

    for arg in arguments:
        for elm in arg:
            # print(elm[-2]+elm[-1])
            dictionary[elm[-2]+elm[-1]] += elm + " "

    for elm in dictionary:
        new_list = dictionary.get(elm).split(" ")
        new_list.pop()
        my_list.append(new_list)
    return my_list


def main():
    print(rhyme_group(['ana', 'banana', 'carte', 'arme', 'parte', 'tare', 'masina']))


if __name__ == "__main__":
    main()
