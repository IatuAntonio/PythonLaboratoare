import os


def file_extension(my_path):
    os.chdir(my_path)
    my_extensions = []
    for file in os.listdir():
        # print(file)
        split_tup = os.path.splitext(file)
        fe = split_tup[-1]
        if fe != '':
            my_extensions.append(fe)

    my_extensions.sort()
    print(my_extensions)


def main():
    my_path = "D:\\Multe chestii\\Antonio\\Facultate\\Python\\PythonLaboratoare\\Lab4\\ex1\\myFolder"
    file_extension(my_path)


if __name__ == "__main__":
    main()
