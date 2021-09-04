name = input('Name: ')
surname = input('Surname: ')
ru = input('Enter the last two numbers of your RU: ')

def emailGenerator(name:str, surname:str, ru:int):
    if len(name) > 0 and len(surname) > 0 and len(ru) > 0:
        email = name[0].lower() + surname.lower() + ru + '@algoritmos.com.br'
        return f'Sr(a) {name} {surname}, your email is: {email}'
    else :
        print('[ERROR] Missing data! Please try again.')
        
print(emailGenerator(name,surname,ru))