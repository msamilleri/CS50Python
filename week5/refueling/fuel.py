
def main():
    fuel_amount = input("Fraction:")
    fuel_gauge = convert(fuel_amount)
    fuel_gauge_str = gauge(fuel_gauge)
    print(fuel_gauge_str)


def convert(fraction):
    while True:
        try:
            result=0
            fuel_amount=fraction.split("/")
            if fuel_amount[1] == '0':
                raise ZeroDivisionError
            if fuel_amount [0] == '0':
                raise ValueError
            if fuel_amount[0].isnumeric():
                (result)=int((int(fuel_amount[0])/int(fuel_amount[1]))*100)
                return result
                break
        except (ValueError, ZeroDivisionError):
               break

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    if percentage >= 99:
        return 'F'
    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()