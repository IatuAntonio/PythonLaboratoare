'''
poti sa salvezi cifrele ca si caractere intr-un string si apoi sa castezi direct la int string ul respectiv.
'''

def extract_numbers(text):
    ok = 0
    number = 0
    for i in range(0, len(text)):
        if text[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            print(True)
            dig = int(text[i])
            number = number * 10 + dig
            ok = 1
        else:
            if ok == 1:
                break

    return number


text = input()

print(extract_numbers(text))
