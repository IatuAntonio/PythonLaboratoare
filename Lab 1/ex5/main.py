'''
ar fi bine daca ai reusi sa faci sa mearga pe mai multe dimensiuni, nu doar fixa de 4.
'''

array = []

for i in range(4):
    text = input()
    array.append(text)

print(array[0], end = "")

for i in range(1, 4):
    print(array[i][3], end = "")

for i in range(2, 4):
    print(array[3][i*(-1)], end = "")

for i in range(1, 4):
    print(array[i * (-1)][0], end = "")

for i in range(1, 3):
    print(array[1][i], end = "")

print(array[2][2], end = "")
print(array[2][1], end = "")


