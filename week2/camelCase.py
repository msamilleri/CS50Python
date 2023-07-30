##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################
"""
camelCase = input('camelCase:')
print("snake_case:",end="")
for c in camelCase:
    if c.isupper():
        new_charter = '_'+c.lower()
        print(camelCase.replace(c,new_charter),end="")
    else:
        print(c,end='')
"""
def cameşCase():
    camelCase = input('camelCase:')
    print("snake_case:",end="")
    for c in camelCase:
        if c.isupper():
            print('_',end="")
        print(c.lower(),end='')
    print()

cameşCase()







