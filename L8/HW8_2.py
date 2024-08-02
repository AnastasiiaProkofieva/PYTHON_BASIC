def is_palindrome(text):
    import string

    text1 = text.lower().split()
    text1 = ''.join(text1)
    for p in string.punctuation:
        if p in text1:
            text1 = text1.replace(p, '')

    str_new = text1[::-1]
    if str_new == text1:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
