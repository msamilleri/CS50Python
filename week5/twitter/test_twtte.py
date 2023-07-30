from twitter import  twitter_test

def main():
    test()

def test():
    assert  twitter_test('Twitter') == 'Twttr'
    assert  twitter_test("What's your name?") == "Wht's yr nm?"


if __name__ == '__main__':
    main()
