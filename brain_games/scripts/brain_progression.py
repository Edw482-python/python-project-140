from brain_games.cli_aux import welcome_user_aux
import random


def main():
    nombre = welcome_user_aux('progression')
    for q in range(3):
        num_ini = random.randint(1, 100)
        longitud = random.randint(5, 10)
        progresion = random.randint(2,4)
        lista = [num_ini + progresion * i for i in range(longitud)]
        pos_oculto = random.randint(0, longitud - 1)
        respuesta = lista[pos_oculto]
        lista[pos_oculto] = ".."
        print(f'Question: {" ".join(map(str, lista))}')
        respuesta_usuario = input('Your answer: ')  
        if respuesta_usuario == str(respuesta):
            print('Correct!')
        else:
            print(f"is wrong answer ;(. correct answer was {respuesta}. Let's try again, {nombre}!")
            break
    else:
        print(f'Congratulations, {nombre}!')

    if __name__ == "__main__":
        main()