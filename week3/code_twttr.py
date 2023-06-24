twitter = input("Input :")
new_word=''
for c in twitter:
    if (c == 'A' or c =='a') or ( c == 'E' or c =='e') or ( c == 'I'  or c =='i' ) or (c == 'O' or c =='o') or (c == 'U' or c =='u') :
        new_word=(twitter.replace(c,''))
print("Outpur:",new_word)