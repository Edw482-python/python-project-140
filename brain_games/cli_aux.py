def welcome_user_aux(select_game):
    #name = prompt.string('May I have yor name?') No me funciono de esta manera...   
    print("Welcome to the Brain Games!")
    name = input('May I have your name?')
    while name.strip() == '':
        name = input('May I have your name? ')
    
    if select_game == 'even':
        print(f'hello, {name}! Answer "yes" if the number is even, otherwise answer "no".')
    if select_game == 'calc':
        print(f'hello, {name}! What is the result of the expression?')
    if select_game == 'gcd':
        print(f'hello, {name}! Find the greatest common divisor of given numbers.')    
    if select_game == 'progression':    
        print(f'hello, {name}! What is the missing number in the progression?')
    if select_game == 'prime':
        print(f'hello, {name}! Answer "yes" if given number is prime. Otherwise answer "no".')
    return name
    