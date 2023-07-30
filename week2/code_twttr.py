##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################


def twitter():
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    sentes = input("Input:")
    print("Output:", end='')
    for char in sentes:
        if char in vowels:
            pass
        else:
            print(char, end="")
    print('')

twitter()