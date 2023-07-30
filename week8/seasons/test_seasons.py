from week8.seasons import seasons as ss


def main():
    test_default_date_print_minutes()
def test_default_date_print_minutes():
    assert ss.main("1995-07-01") == "Fourteen million, seven hundred fifty-eight thousand, five hundred sixty minutes"



if __name__ == '__main__':
    main()