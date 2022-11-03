import os

my_extensions = []


def count_extensions(my_path):
    ext_counter = []
    if os.path.isdir(my_path):

        for file in os.listdir(my_path):
            if os.path.isdir(os.path.join(my_path, file)):
                count_extensions(os.path.join(my_path, file))

            if not os.path.isdir(os.path.join(my_path, file)):
                split_tup = os.path.splitext(file)
                fe = split_tup[-1]
                my_extensions.append(fe)
        my_set = set(my_extensions)
        for i in my_set:
            ext_counter.append((i, my_extensions.count(i)))
            ext_counter.sort(key=lambda tup: tup[1])
            ext_counter.reverse()
        return ext_counter
    else:
        letters = []
        file = open(my_path, "r")
        lines = file.read()
        for i in range(-20, 0):
            letters.append(lines[i])
        return letters


def main():
    my_path = "fisier.txt"
    print(count_extensions(my_path))


if __name__ == "__main__":
    main()
