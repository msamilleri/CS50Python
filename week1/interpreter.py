##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################
expression=input('Expression:')
x,y,z = expression.split(' ')
x=float(x)
z=float(z)
if y == '+':
    print(round(x+z,2))
elif y == '-':
    print(round(x-z,2))
elif y == '/':
    print(round(x/z,2))
elif y == '*':
    print(round(x*z,2))
else:
    print('ERROR 404')
