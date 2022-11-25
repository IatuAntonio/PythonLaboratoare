import re


def my_fnc(my_path, attrs):
    my_list = []
    fd = open(my_path, "r")
    txt = fd.readlines()
    for element in txt:
        cnt = 0
        for atr in attrs.items():
            if re.search(atr[0]+"\s*=\s*\""+atr[1]+"\"", element):
                cnt += 1
        if cnt != 0:
            my_list.append(element)
    for el in my_list:
        print(el)


def main():
    my_path = "D:\\Multe chestii\\Antonio\\Facultate\\Python\\PythonLaboratoare\\Lab6\\ex05\\file.txt"
    my_fnc(my_path, {"class": "planta", "url": "google.com", "name": "cd"})


if __name__ == "__main__":
    main()
