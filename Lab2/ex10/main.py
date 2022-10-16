def take_elements(*arguments):
    new_list = []
    maxim = -1
    for arg in arguments:
        if maxim < len(arg):
            maxim = len(arg)

    for arg in arguments:
        my_list = []
        for elements in arg:
            my_list.append(elements)
        while len(my_list) < maxim:
            my_list.append(None)
        new_list.append(my_list)
    tuples = []
    for i in range(0, maxim):
        my_list = []
        for arg in new_list:
            my_list.append(arg[i])
        tuples.append(my_list)
    return tuples

    # cnt = 0
    # while 1:
    #     elements = []
    #     counter = 0
    #     for arg in arguments:
    #         if cnt == len(arg):
    #             break
    #         elements.append(arg[cnt])
    #         if arg is None:
    #             counter += 1
    #     if counter == len(elements):
    #         break
    #     new_list.append(tuple(elements))
    #     cnt += 1
    #
    # return new_list


def main():

    print(take_elements([1, 2, 3], [5, 7], ["a", "b", "c"], [4, 2, 5, 6]))


if __name__ == "__main__":
    main()
