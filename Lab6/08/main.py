import re
import os


def my_fnc(my_path):
    os.chdir(my_path)

    files = []
    for file in os.listdir():
        cnt = 0
        fd = open(file, "r")
        txt = fd.read()
        if re.match(r"[1-8][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|[1-4][0-8])([0-9][0-9][0-9])[0-9]",txt):
            cnt += 1
        split_tup = os.path.splitext(file)
        fe = split_tup[0]
        if fe != '':
            if re.match(r"[1-8][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|[1-4][0-8])([0-9][0-9][0-9])[0-9]",fe):
                cnt += 1
            if cnt == 2:
                print(">>", file)
            if cnt == 1:
                print(file)
            files.append(fe)
    # print(files)


def main():
    my_path = "D:\\Multe chestii\\Antonio\\Facultate\\Python\\PythonLaboratoare\\Lab6\\ex08\\unFolder"
    my_fnc(my_path)


if __name__ == "__main__":
    main()
