def main ():
    x=get_fuel()
def get_fuel():
    while True:
        try:
            result=0
            fuel_amount=(input("Fraction:"))
            fuel_amount=fuel_amount.split("/")
            if fuel_amount[1] == '0':
                raise ZeroDivisionError
            if fuel_amount [0] == '0':
                raise ValueError
            if fuel_amount[0].isnumeric():
                (result)=int((int(fuel_amount[0])/int(fuel_amount[1]))*100)
                if result == 100:
                    print("F")
                    break
                else:
                    print(f"{result}%")
                    break
        except (ValueError, ZeroDivisionError):
               pass
        else:
            pass
    return result

main()
