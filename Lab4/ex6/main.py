import os

files_list = []


def callback_fnc(target):
    try:
        if "txt" not in target and not os.path.isdir(target):
            raise Exception("Fisierul nu este text")
    except Exception as e:
        print("Fisierul nu este un document text")


def find_string(target, to_search, callback):
    # print(target)
    # if "txt" not in target and not os.path.isdir(target):

    if os.path.isdir(target):
        for file in os.listdir(target):
            # os.chdir(target)
            find_string(os.path.join(target, file), to_search, callback)

    callback(target)

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
    my_path = "myFolder"
    print(find_string(my_path, "ceva", callback_fnc))


if __name__ == "__main__":
    main()
