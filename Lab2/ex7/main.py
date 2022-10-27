'''
aici puteai sa adaugi toate numerele care sunt palindroame intr-o lista si sa aplici max() si len() peste lista
'''


def palindrome_function(numbers):
    cnt = 0
    maxim = -1
    my_param = []
    for i in numbers:
        if i == i[::-1]:
            cnt += 1

            try:
                nr = int(i)
            except ValueError:
                print("Nu ai introdus numere!!!")
                return

            if maxim < nr:
                maxim = nr
    my_param = (cnt, maxim)
    return my_param


def main():
    txt = input("Your numbers:\n")
    my_list = txt.split(" ")
    ml = palindrome_function(my_list)
    if ml is not None:
        print(ml)


if __name__ == "__main__":
    main()
