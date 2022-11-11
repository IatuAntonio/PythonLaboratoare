def sum_k_a(*args1, **args2):
    suma = 0
    for element in args2.values():
        suma += element

    return suma


def main():
    f = (lambda *args1, **args2: sum(args2.values()))
    print(f(1, 2, c=3, d=7))
    print(sum_k_a(1, 2, c=3, d=4))


if __name__ == "__main__":
    main()
