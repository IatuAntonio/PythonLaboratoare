from math import sqrt


def process_item(x):
    def test_prime(nr):
        if nr == 0 or nr == 1:
            return 0

        for i in range(2, int(sqrt(nr)) + 1):
            if nr % i == 0:
                return 0

        return 1

    ok = 0

    while not ok:
        x += 1
        if test_prime(x) == 1:
            ok = 1
    return x


# print(process_item(90))
