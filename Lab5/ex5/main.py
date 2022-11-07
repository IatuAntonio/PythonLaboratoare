def my_function(a_list):
    my_list = []
    for element in a_list:
        if isinstance(element, int) or isinstance(element, float):
            my_list.append(element)

    print(my_list)


def main():
    my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])
    

if __name__ == "__main__":
    main()
