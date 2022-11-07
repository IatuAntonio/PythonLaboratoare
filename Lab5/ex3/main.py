def vowels(var):
    if var in "aeiou":
        return True
    else:
        return False


def main():
    text = "antonio ceva unde"

    print(list(filter(lambda x: x[0] in "aeiou", text)))

    filtru = filter(vowels, text)
    print(list(filtru))

    my_list = [v for v in text if v in "aeiou"]
    print(my_list)


if __name__ == "__main__":
    main()
