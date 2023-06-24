
hello_text = input('Greeting: ')
if hello_text.startswith('hello') or hello_text.startswith('Hello'):
    print('$0')
elif hello_text.startswith('How'):
    print('$20')
else:
    print('$100')
