import string

alf = input('Please type two letters using "-" between them: ')
text = alf.split('-')

alphabet = string.ascii_letters

for el in alphabet:
    if text[-1] == el:
        x = alphabet.index(el)
        res = alphabet[alphabet.index(text[0]):(x+1)]
        print(res)
