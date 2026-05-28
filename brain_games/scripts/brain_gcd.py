from brain_games.cli_aux import welcome_user_aux
import math
import random



def main():
    nombre = welcome_user_aux('gcd')
    for q in range(3):
        a, b = random.randint(1, 100), random.randint(1, 100)
        print(f'Question: {a} {b}')
        respuesta = input('Your answer: ')
        if respuesta == str(math.gcd(a, b)):
            print('Correct!')
        else:
            print(f'is wrong answer ;(. correct answer was {math.gcd(a, b)}.')
            break
    else:
        print(f'Congratulations, {nombre}!')




if __name__ == "__main__":
    main()