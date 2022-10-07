def counter(number):
    cnt = 0
    for i in range(len(number)):
        if number[i] == '1':
            cnt += 1

    return cnt


number = input()
number = bin(int(number)).replace("0b", "")

print(counter(number))
