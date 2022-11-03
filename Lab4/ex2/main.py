import os


def fill_file(directory, file):
    fd = open(file, "w")
    os.chdir(directory)
    my_files = []
    for file in os.listdir():
        my_files.append(os.path.abspath(file))
        fd.write(os.path.abspath(file) + "\n")

    # print(my_files)
    fd.close()


def main():
    my_directory = "D:\\Multe chestii\\Antonio\\Facultate\\Python\\PythonLaboratoare\\Lab4\\ex1\\myFolder"
    my_file = "myFile.txt"
    fill_file(my_directory, my_file)


if __name__ == "__main__":
    main()
