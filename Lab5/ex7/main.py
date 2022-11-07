def sum_digits(x):
    return sum(map(int, str(x)))


def fibo(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return fibo(nr-1) + fibo(nr-2)


def process(**args):
    fibo_list = []
    right_list = []
    # revin
    # for i in range(0, 1001):
    #     fibo_list.append(fibo(i))
    #
    # for element in args:
    #     if element == "filters":
    #         ceva = args.values()
    #         ceva(fibo_list)
    #
    # for element in args:
    #     if element == "offset":
    #         cnt = args.values()
    #         while cnt:
    #             fibo_list.pop(0)
    #             cnt -= 1
    #
    # for element in args:
    #     if element == "limit":
    #         cnt =
    #         cnt = int(cnt)
    #
    #         while cnt:
    #             right_list.append(fibo_list[cnt-1])
    #             fibo_list.pop(0)
    #             cnt -= 1

def main():
    process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],   limit=2, offset = 2)


if __name__ == "__main__":
    main()
