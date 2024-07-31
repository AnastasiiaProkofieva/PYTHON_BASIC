def correct_sentence(text):
    text_lst = text.split()
    text_lst[0] = text_lst[0].title()
    correction = " ".join(text_lst)
    correction_lst = correction.split('.')
    if correction_lst[-1] != '':
        correction = f'{correction}.'
    return correction


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
