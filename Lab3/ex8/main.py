def loop(d):
    key_list = []
    dictionary = {}
    for i in d.keys():
        dictionary[i] = 0
        key_list.append(i)

    ok = 1
    cnt = key_list[0]
    lista = []
    while ok:
        if dictionary[cnt] == 0:
            if d[cnt] not in lista:
                lista.append(d[cnt])
            # print(d[cnt])
            dictionary[cnt] = 1
            cnt = d[cnt]
        else:
            break

    print(lista)


def main():
    loop({"start": "a", "b": "a", "a": "6", "6": "z", "x": "2", "z": "2", "2": "2", "y": "start"})


if __name__ == "__main__":
    main()
