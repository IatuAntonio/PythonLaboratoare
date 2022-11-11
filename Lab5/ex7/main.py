def sum_digits(x):
    return sum(map(int, str(x)))


def fibo():
    a = 0
    b = 1
    fibo_list = [a, b]
    for i in range(1, 100):
        c = a + b
        fibo_list.append(c)
        a = b
        b = c
    return fibo_list


def process(**args):
    my_list = []
    if "filters" in args.keys():
        my_list = list([el for el in fibo() if args["filters"][0](el) == True])

    if "offset" in args.keys():
        my_list = my_list[args["offset"]+1:]

    if "limit" in args.keys():
        my_list = my_list[:args["limit"]]
    print(my_list)
    return my_list


def main():
    process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2,
            offset=2)


if __name__ == "__main__":
    main()
