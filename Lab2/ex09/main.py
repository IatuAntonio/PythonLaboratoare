def can_see(matrix):
    my_list = []
    n = len(matrix)
    m = len(matrix[0])

    for j in range(0, m):
        maxim = -1
        for i in range(0, n):
            if matrix[i][j] > maxim:
                maxim = matrix[i][j]
            elif matrix[i][j] <= maxim:
                my_list.append((i, j))
    return my_list



def main():
    n = input("n = ")
    try:
        n = int(n)
    except ValueError:
        print("N nu este un numar!!!")
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
            print("Nu ai introdus numere!!!")
            return 0
    print(can_see(matrix))


if __name__ == "__main__":
    main()
# 4
# 1 2 3 2 1 1
# 2 4 4 3 7 2
# 5 5 2 5 6 4
# 6 6 7 6 7 5
