def test_dictionary(my_set, d):
    # for arg in my_set:
    #     if arg is not None:
    #         print(d.setdefault(arg[0], 1))
    #         if arg[1] in d.setdefault(arg[0], 1):
    #


def main():
    print(test_dictionary({("key1", "", "inside", ""),
                           ("key2", "start", "middle", "winter")},
                          {"key1": "come inside, it's too cold out",
                           "key3": "this is not valid"}))


if __name__ == "__main__":
    main()
