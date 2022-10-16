from colorama import Fore


def set_operation(f_list, s_list):
    intersection = set()
    union = set()
    f_minus_s = []
    s_minus_f = []
    for i in f_list:
        union.add(i)
        if i in s_list:
            intersection.add(i)
        if i not in s_list:
            f_minus_s.append(i)

    for i in s_list:
        union.add(i)
        if i not in f_list:
            s_minus_f.append(i)

    return intersection, union, f_minus_s, s_minus_f


def main():
    txt1 = input("First list:\n")
    my_list1 = txt1.split(" ")

    txt2 = input("Second list:\n")
    my_list2 = txt2.split(" ")

    first_list = []
    second_list = []
    try:
        for i in my_list1:
            first_list.append(int(i))

        for i in my_list2:
            second_list.append(int(i))
    except ValueError:
        print(f"{Fore.RED}Nu ai introdus numere!!!")
        return 0

    # print(first_list)
    # print(second_list)

    diff1 = []
    diff2 = []
    intersection, union, diff1, diff2 = set_operation(first_list, second_list)

    print(f"\n{Fore.GREEN}"
          f"Intersection: {intersection}\n"
          f"Union: {union}\n"
          f"First minus second: {diff1}\n"
          f"Second minus first: {diff2}"
    )


if __name__ == "__main__":
    main()
