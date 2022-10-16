from colorama import Fore


def modify_matrix(matrix, n):
    for i in range(0, n):
        for j in range(0, i):
            matrix[i][j] = 0
    return matrix


def main():
    n = input("n = ")
    try:
        n = int(n)
    except ValueError:
        print(f"{Fore.RED}N nu este un numar!!!")
        return 0

    matrix = []
    for i in range(0, n):
        txt = input()
        my_list = txt.split(" ")
        numbers = []
        try:
            for j in my_list:
                numbers.append(int(j))
            matrix.append(numbers)
        except ValueError:
            print(f"{Fore.RED}Nu ai introdus numere!!!")
            return 0

    matrix = modify_matrix(matrix, n)
    for i in matrix:
        print(i)


if __name__ == "__main__":
    main()