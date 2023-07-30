##########################################
#                                        #
#       author:@msamilleri               #
#       you can use in your project      #
#                                        #
##########################################

def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 1:
        return  False
    if (len(s)>=2) or len(s) <= 6 :
        for num in range(len(s)):
            if not s[0].isnumeric() and not s[1].isnumeric():
                if s[-1].isnumeric():
                    if s[num].isnumeric():
                        if s[num] == 0:
                            return False
                        else:
                            return False
    else:
        return False


if __name__ == '__main__':
    main()


