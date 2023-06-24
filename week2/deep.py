def text():
    test_text=input('What is the Answer to the Great Question of Life, the Universe, and Everything ?')
    if test_text == '42':
        print('Yes')
    elif test_text == 'forty-two':
        print('Yes')
    elif test_text== 'forty two':
        print('Yes')
    else:
        print('No')

text()