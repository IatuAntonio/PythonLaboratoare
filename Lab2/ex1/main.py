from colorama import Fore


def fibonacci(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return fibonacci(nr-1) + fibonacci(nr-2)


n = input("Enter your number: ");

try:
    n = int(n)
    for i in range(0, n):
        print(f"{Fore.CYAN}{fibonacci(i)}", end=" ")
except (ValueError, TypeError) as error:
    print(f"{Fore.RED}Your input is not a number!!!")


