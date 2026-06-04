
def welcome_user():
    #name = prompt.string('May I have yor name?') No me funciono de esta manera...
    name = input('May I have your name? ').strip
    while name.strip() == '':
        name = input('May I have your name? ').strip()
    
    print(f'Hello, {name}!')
    return name