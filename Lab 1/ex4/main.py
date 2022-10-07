def transform_text(text):
    my_text = [text[0].lower()]

    for i in range(1, len(text)):
        if text[i] in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            my_text.append("_")
            my_text.append(text[i].lower())
        else:
            my_text.append(text[i])

    return ''.join(my_text)


text = input()

print(transform_text(text))

