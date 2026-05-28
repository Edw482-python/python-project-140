from brain_games.cli_aux import welcome_user_aux
from brain_games.cli_calcula import operaciones
import random


def main():
    nombre = welcome_user_aux('calc')
    for q in range(3):
        a, b, c = random.randint(1, 100), random.randint(1, 100), random.choice(['+', '-', '*'])
        print(f'Question: {a} {c} {b}')
        respuesta = input('Your answer: ')
        if respuesta == str(operaciones(a, b, c)):
            print('Correct!')
        else:
            print(f'is wrong answer ;(. correct answer was {operaciones(a, b, c)}.')
            break
    else:
        print(f'Congratulations, {nombre}!')


if __name__ == "__main__":
    main()
