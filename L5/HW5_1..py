import keyword
import string

var = input('Please type the variable\'s name: ')

result = 'True'

if not var.islower() or ' ' in var:  # small letters and no space check
    result = 'False'

for n in string.digits:  # start with digit check
    if var[0] == n:
        result = 'False'

for word in keyword.kwlist:  # keywords check
    if '_' in var:
        var_lst = var.split('_')
        for el in var_lst:
            if word == el:
                result = 'True'
    else:
        check = var.find(word)
        if check >= 0:
            result = 'False'

for p in string.punctuation:  # punctuation check
    if p in var:
        if var == '_':
            result = 'True'
        elif var[0] == '_':
            result = 'False'
        elif p != '_':
            result = 'False'

print(result)
