from bank import value
def main():
    test_value()


def test_value():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('How is going') == 20
    assert value('hi') == 100


if __name__ == "__main__":
    main()