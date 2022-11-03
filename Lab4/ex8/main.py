import os


def fill_file(directory):
    os.chdir(directory)
    my_files = []
    for file in os.listdir():
        my_files.append(os.path.abspath(file))

    # print(my_files)
    return my_files


def main():
    my_directory = "D:\\Multe chestii\\Antonio\\Facultate\\Python\\PythonLaboratoare\\Lab4\\ex1\\myFolder"
    print(fill_file(my_directory))


if __name__ == "__main__":
    main()