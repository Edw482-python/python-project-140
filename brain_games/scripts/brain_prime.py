from brain_games.cli_aux import welcome_user_aux
import random
import math

def es_primo(num):
    contador_primo = 0
    for i in range (num):
        if num % (i + 1) == 0:
            contador_primo += 1            
    if contador_primo == 2:
        return(True)
    return(False)


def main():
    nombre = welcome_user_aux('prime')
    for q in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        respuesta_usuario = input('Your answer: ')  
        if es_primo(num) and respuesta_usuario == 'yes':
            print('Correct!')
        elif not es_primo(num) and respuesta_usuario == 'no':
            print('Correct!')
        else:
            print(f"is wrong answer ;(. correct answer was {'yes' if es_primo(num) else 'no'}. Let's try again, {nombre}!")
            break
    else:
        print(f'Congratulations, {nombre}!')

    if __name__ == "__main__":
        main()