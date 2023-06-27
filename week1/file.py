file_text = input('File name: ')

file_text = file_text.lower().strip().split('.')
print(file_text)
match  file_text[1]:
    case 'gif':
        print('image/',file_text[1])
    case 'jpg':
        print('image/', file_text[1])
    case 'jpeg':
        print('image/',file_text[1])
    case 'png':
        print('image/',file_text[1])
    case 'pdf':
        print('image/',file_text[1])
    case 'tct':
        print('image/',file_text[1])
    case 'zip':
        print('image/',file_text[1])

