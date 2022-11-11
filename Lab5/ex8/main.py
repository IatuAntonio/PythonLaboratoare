def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def fnc(*args1, **args2):
        val = function(*args1, **args2)
        print(f"Arguments are: {args1}, {args2} will return {val}")
        return val
    return fnc


def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    def fnc(*args1, **args2):
        val = function(*args1, **args2)
        print(val)
        return 2 * val
    return fnc


def main():
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)

    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)

    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)


if __name__ == "__main__":
    main()
