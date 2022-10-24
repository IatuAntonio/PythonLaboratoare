def equal_d(d1, d2):
    ok = True
    for i in d1.items():
        # print(i[0])
        j = d2.keys()
        if i[0] not in j:
            ok = False
        else:
            if i[1] not in d2.values():
                ok = False
    return ok


def main():
    print(equal_d({"a": 3, "b": 4, "c": ["a", "b", "c"]}, {"d": "ceva", "r": 42}))


if __name__ == "__main__":
    main()
