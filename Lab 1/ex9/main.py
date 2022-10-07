
text = input()

array = []

for i in range(0, 123):
    array.append(0)

for i in range(len(text)):
    array[ord(text[i])] += 1

maxim = -1
c = ''

for i in range(65, 123):
    if (array[i] > maxim):
        maxim = array[i]
        c = i

print(chr(c))