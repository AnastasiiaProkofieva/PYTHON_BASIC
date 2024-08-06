def popular_words(text, words):
    text = text.lower().split()
    dict_new = {}
    for key in words:
        dict_new[key] = text.count(key)
    return dict_new


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
