from random import randint
def guess_number():
    level_input = int(input("Input:"))
    while True:
        guess_input =  int(input("Guess:"))
        rand_number = randint(1,level_input)
        print(rand_number)
        if guess_input<rand_number:
            print("Too small!")
        elif guess_input>rand_number:
            print("Too large!")
        elif guess_input == rand_number:
            print("Just right!")
            break
        else:
            print("ERROR 404")


guess_number()