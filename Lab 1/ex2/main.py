'''
e in regula, ai putea in loc de functie sa faci direct verificarea.
'''

def vowel(chr):
    return chr in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


def cnt_vowels(text):
    cnt = 0
    for i in range(0, len(text)):
        if vowel(text[i]):
            cnt += 1

    return cnt


text = input()

print(cnt_vowels(text))
