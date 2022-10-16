from colorama import Fore


def test_prime(nr):
    if nr <= 1:
        return -1
    else:
        for i in range(2, (nr // 2) + 1):
            if nr % i == 0:
                return -1
                break

    return 1


def prime_list(number_list):
    new_list = []
    for i in number_list:
        if test_prime(i) == 1:
            new_list.append(i)
    return new_list


def main():
    txt = input("Give me your list:\n")
    my_list = txt.split(" ")
    numbers = []
    try:
        for i in my_list:
            numbers.append(int(i))
    except ValueError:
        print(f"{Fore.RED}Nu ai introdus numere!!!")
        return 0

    numbers = prime_list(numbers)
    print(f"{Fore.GREEN}{numbers}")


if __name__ == "__main__":
    main()
