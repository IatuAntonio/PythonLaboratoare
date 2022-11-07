def my_function(a_list):
    even = []
    odd = []
    my_list = []
    for element in a_list:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)

    for i in even:
        my_list.append((i, odd[0]))
        odd.pop(0)

    print(my_list)


def main():
    my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])


if __name__ == "__main__":
    main()
