

camelCase = input('camelCase:')
for c in camelCase:
    if c.isupper():
        new_charter = '_'+c.lower()
        snake_case =camelCase.replace(c,new_charter)
        print('snake_case:'+snake_case)
    if c.islower():
       print('snake_case:',camelCase)
       pass







