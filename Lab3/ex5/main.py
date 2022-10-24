def test_dictionary(my_set, d):
    my_keys = []
    for arg in my_set:
        my_keys.append(arg[0])
    for arg in d.keys():
        if arg not in my_keys:
            return 0
    ok = 1
    for arg in my_set:
        val_d = d.setdefault(arg[0], None)
        if val_d is not None:
            if arg[1] != val_d[:len(arg[1])]:
                ok = 0
            mdd = len(val_d) - len(arg[3])
            if arg[2] not in val_d[len(arg[1]):mdd]:
                ok = 0
            if arg[3] != val_d[mdd:]:
                ok = 0
        if ok == 1 and arg[0] is not None:
            print(arg[0])
    if ok:
        return 1
    else:
        return 0



def main():
    print(test_dictionary({("key1", "", "inside", ""),
                           ("key2", "start", "middle", "winter")},
                          {"key1": "come inside, it's too cold out",
                           "key3": "this is not valid"}))


if __name__ == "__main__":
    main()
