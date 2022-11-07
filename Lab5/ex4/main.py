def my_function(*args1, **args2):
    d = {}
    my_list = []
    for element in args1:
        cnt = 0
        test = 0
        if isinstance(element, dict):
            for k, v in element.items():
                cnt += 1
                if isinstance(k, str):
                    if len(k) > 2:
                        test = 1
                # print(k, " ", v)
        if test == 1 and cnt > 1:
            my_list.append(element)

    for element in args2.values():
        cnt = 0
        test = 0
        if isinstance(element, dict):
            for k, v in element.items():
                cnt += 1
                if isinstance(k, str):
                    if len(k) > 2:
                        test = 1
                # print(k, " ", v)
        if test == 1 and cnt > 1:
            my_list.append(element)

    print(my_list)


def main():
    my_function({1: 2, 3: 4, 5: 6,}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})


if __name__ == "__main__":
    main()
