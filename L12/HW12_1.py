import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        text = '<'
        while text in html:
            i1 = int(html.find('<'))
            i2 = int(html.find('>'))
            string = html[i1:i2 + 1]
            html = html.replace(string, '')
        html_lst = html.split('\n')
        lst =[]
        for el in html_lst:
            if not el.isspace() and el != '':
                lst.append(el)
        html = '\n'.join(lst)
    with open('cleaned.txt', 'w') as outfile:
        for line in html:
            outfile.write(line)
    return html


print(delete_html_tags('draft.html'))
