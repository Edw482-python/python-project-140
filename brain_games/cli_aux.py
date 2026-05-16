def welcome_user_aux():
    #name = prompt.string('May I have yor name?') No me funciono de esta manera...
    name = input('May I have your name? ')
    while name.strip() == '':
        name = input('May I have your name? ')
    
    print(f'hello, {name}! Answer "yes" if the number is even, otherwise answer "no".')
    return name
    