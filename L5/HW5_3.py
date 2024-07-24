# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string

str_1 = input('Please type your string: ')
str_lst = str_1.title().split()
str_2 = ''.join(str_lst)

for p in string.punctuation:
    if p in str_2:
        str_2 = str_2.replace(p, '')

str_new = str_2[:139]
print('#' + str_new)
