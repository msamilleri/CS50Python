


def main():
    plate_input = input('')
    is_plate = is_valid(plate_input)
    if is_plate == 'True':
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    if  len(s)<=2 or len(s) <= 6 :
        if s[4:6].isnumeric():
            if s[5:] != 0:
                return 'True'

    else:
        return 'False'


if __name__ == "__main__":
    main()