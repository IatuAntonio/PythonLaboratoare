'''
e muncitoreasca metoda, dar e in regula. ceva mai interesant ai putea face cu manipulari de string uri, maybe vezi ceva in curs si ai putea rezulva in 1,2,3 linii
'''

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
