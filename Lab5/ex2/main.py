def sum_k_a(*args1, **args2):
    sum = 0
    for element in args2.values():
        sum += element

    return sum


def main():
    # revin
    # f = lambda *args1, **args2: args2.values
    # print(f(1, 2, c=3, d=4))
    print(sum_k_a(1, 2, c=3, d=4))


if __name__ == "__main__":
    main()
