def count_numbers(my_string):
    d = {}
    for i in range(0, len(my_string)):
        d[my_string[i]] = 0

    for i in range(0, len(my_string)):
        d[my_string[i]] += 1
    return d


def main():
    print(count_numbers("ana are mere pere si prune"))


if __name__ == "__main__":
    main()
