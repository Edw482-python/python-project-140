from brain_games.cli_aux import welcome_user_aux
import random


def main():
    nombre = welcome_user_aux()
    for q in range(3):
        numero = random.randint(1, 100)
        print(f'Question: {numero}')
        respuesta = input('Your answer: ')
        if numero % 2 == 0 and respuesta.lower() == 'yes' or numero % 2 != 0 and respuesta.lower() == 'no':
            print('Correct!')
        else:
            print('Incorrect!')
            break
    else:
        print(f'Congratulations, {nombre}!')
