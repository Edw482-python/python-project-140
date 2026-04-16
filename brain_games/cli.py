import prompt

def welcome_user():
    #name = prompt.string('May I have yor name?') No me funciono de esta manera...
    name = input('May I have your name? ')
    while name.strip() == '':
        name = input('May I have your name? ')
    
    print(f'hello, {name}!')