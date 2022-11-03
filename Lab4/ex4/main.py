import os
import sys


def get_extensions(my_path):
    # adaug extensiile o singura data
    # extensions = set()
    # for file in os.listdir(my_path):
    #     split_tup = os.path.splitext(file)
    #     fe = split_tup[-1]
    #     if fe != "":
    #         extensions.add(fe)
    # print(extensions)

    # adaug extensiile care se regasesc doar o data

    extensions = []
    test = set()

    for file in os.listdir(my_path):
        split_tup = os.path.splitext(file)
        fe = split_tup[-1]
        if fe != "":
            extensions.append(fe)
            test.add(fe)

    my_ext = set()
    for i in test:
        if i in extensions:
            extensions.remove(i)
        if i not in extensions:
            my_ext.add(i)
    print(my_ext)


def main():
    my_path = sys.argv[1]
    get_extensions(my_path)


if __name__ == "__main__":
    main()
