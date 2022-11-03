import os


def get_details(my_path):
    dictionary = {"full_path": os.path.abspath(my_path)}

    size = os.path.getsize(my_path)

    dictionary["file_size"] = size

    split_tup = os.path.splitext(my_path)
    fe = split_tup[-1]

    dictionary["file_extension"] = fe

    fd = open(my_path, "w")
    dictionary["can_write"] = fd.writable()
    fd.close()
    fd = open(my_path, "r")
    dictionary["can_read"] = fd.readable()
    fd.close()

    print(dictionary)


def main():
    my_path = "poza.png"
    get_details(my_path)


if __name__ == "__main__":
    main()
