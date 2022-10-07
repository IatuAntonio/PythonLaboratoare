def counter(text1, text2):
    cnt = 0
    for i in range(0, len(text2)-len(text1)+1):
        if text1 in text2[i:i+len(text1)]:
            cnt += 1

    return cnt


first_text = input()
second_text = input()

print(counter(first_text, second_text))
