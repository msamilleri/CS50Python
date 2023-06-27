def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s)<=2 or len(s) <= 6 :
        if s[4:6].isnumeric():
            if s[5:] != 0:
                return True

    else:
        return False
main()

