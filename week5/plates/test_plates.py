from plates import is_valid


def main():
    test_plates()
def test_plates():
    assert is_valid('CSAA05') == 'False'
    assert is_valid('CS50PQ') == 'False'
    assert is_valid('PI3.14') == 'False'


if __name__ == '__main__':
    main()