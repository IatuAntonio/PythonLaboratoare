def my_function(*arguments, **args):
    cnt = 0
    for arg in arguments:
        val = args.values()
        if arg in val:
            cnt += 1

    print(cnt)


def main():
    my_function(1, 2, 3, 4, x=2, y=2, z=3, w=5)


if __name__ == "__main__":
    main()
