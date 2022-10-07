def palindrom(number):
    aux = number
    num1 = number % 10
    number //= 10
    while number:
        dig = number % 10
        num1 = (num1 * 10) + dig
        number //= 10

    print(num1)
    if num1 == aux:
        return True
    else:
        return False


text = input()
my_number = int(text)
print(palindrom(my_number))
