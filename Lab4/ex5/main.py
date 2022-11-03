import os

files_list = []


def find_string(target, to_search):
    # print(target)
    if "txt" not in target and not os.path.isdir(target):
        raise Exception("Fisierul nu este text")
    if os.path.isdir(target):
        for file in os.listdir(target):
            # os.chdir(target)
            find_string(os.path.join(target, file), to_search)

    if not os.path.isdir(target) and "txt" in target:
        my_file = target.split("\\")
        main_path = os.path.dirname(__file__)
        file_path = os.path.join(main_path, target)

        fd = open(file_path, "r")
        text = fd.read()
        # print(text)
        if to_search in text:
            # print(1)
            files_list.append(target)
        fd.close()
    return files_list


def main():
    my_path = "myFolder - Copy"
    print(find_string(my_path, "ceva"))


if __name__ == "__main__":
    main()
