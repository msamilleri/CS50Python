def main():
    hello_text = input('Greeting: ')
    print(value(hello_text))


def value(greeting):

    if greeting.startswith('hello') or greeting.startswith('Hello'):
        return 0
    elif greeting.startswith('How'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()