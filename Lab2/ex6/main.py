from colorama import Fore


def test_function(matrix, x):
    dictionary = {}
    new_list = set()
    for i in matrix:
        for j in i:
            dictionary[j] = 0

    for i in matrix:
        for j in i:
            dictionary[j] += 1

    for i in matrix:
        for j in i:
            if dictionary[j] == x:
                new_list.add(j)
    return new_list


def main():
    matrix = []
    x = 0
    while 1:
        txt = input()
        my_list = txt.split(" ")

        if len(my_list) == 1:
            x = my_list[0]
            try:
                x = int(x)
            except ValueError:
                print(f"{Fore.RED}N nu este un numar!!!")
                return 0
            break
        matrix.append(my_list)

    print(test_function(matrix, x))







    #test_function(1, 2, 3, 3, 4, 5, 2, 3, x=x)


if __name__ == "__main__":
    main()