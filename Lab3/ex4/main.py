def build_xml_element(tag, content, d):
    my_string = []
    my_text = []
    my_string.append(f"<{tag} ")
    for arg in d:
        # my_string.append()
        my_string.append(f"{arg}=\"{d[arg]}\" ")

    my_string.append(f">{content}</{tag}>")
    cnt = 0
    print("".join(my_string))
    # for i in my_string:
    #     for j in i:
    #         my_text.append(j)
    # print(my_text)


def main():
    build_xml_element("a", "Hello there", {"href": "http://python.org", "_class": "my-link", "id": "someid"})
    build_xml_element("div", "Ana are mere", {"_class": "my-link", "id": "someid", "lang": "en", "title": "text"})


if __name__ == "__main__":
    main()
