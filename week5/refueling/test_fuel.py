from refueling.fuel import gauge, convert


def main():
    tes_convert()
    test_gauge()
    test_sustem()
def tes_convert():
    assert convert('1/4') == 25
    assert convert('2/4') == 50
    assert convert('3/4') == 75
    assert convert('4/4') == 100

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(35) == '35%'
    assert gauge(55) == '55%'
    assert gauge(100) == 'F'

def test_sustem():
    assert gauge(convert('1/4')) == '25%'
    assert gauge(convert('3/4')) == '75%'
    assert gauge(convert('5/10')) == '50%'
    assert gauge(convert('4/4')) == 'F'

if __name__ == '__main__':
    main()