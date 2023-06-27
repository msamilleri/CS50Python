
from random import randint as rd
def main():
    right_number=0
    game_counter=10
    game_level = get_level()
    while game_counter>0:
        if (1<=game_level) and (game_level <=3):
            number_1 = generate_integer(game_level)
            number_2 = generate_integer(game_level)
            result=number_1+number_2
            print(f"{number_1}+{number_2} =",end='')
            guess_number = int(input())
            if result != guess_number:
                print("EEE")
                game_counter-=1
            else:
                right_number+=1
                game_counter -= 1
        else:
            game_level=get_level()

    if game_counter==0:
        print("Scroce :",right_number)
def get_level():
    level=0
    while True:
        try:
            level=int(input("Level:"))
        except ValueError:
            pass
        else:
            break
    return level


def generate_integer(level):
    if level == 1:
        return rd(1,10)
    elif level == 2:
        return  rd(1,20)
    elif level == 3:
        return  rd(1,30)
    else:
        return ("Error")


if __name__ == "__main__":
    main()