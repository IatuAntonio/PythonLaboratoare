'''
incearca sa validezi input ul sa ai numere la input. dar da, in rest ar fi bine
'''

def calculate_gcd(x, y):

    while y:
        aux = y
        y = x % y
        x = aux

    return x


text = input()
my_list = text.split(" ")

a = int(my_list[0])
b = int(my_list[1])
gcd = calculate_gcd(a, b)

for i in range(2, len(my_list)):
    num = int(my_list[i])
    gcd = calculate_gcd(gcd, num)

print(gcd)
