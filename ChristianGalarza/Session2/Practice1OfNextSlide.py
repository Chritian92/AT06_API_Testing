print("Example: This is my web page http://holamundo.html ")
text = input('Enter a String with a url please ')
print("*****************************************************")


def valid_link(text):
    end_url = text.split(" ")
    for url in end_url:
        if url.lower().startswith('http://'):
            print("Is a valid url {} ".format(url))


valid_link(text)
