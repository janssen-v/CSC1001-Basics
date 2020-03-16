def greet(lang):
    if lang=='es':
        return('Hola')
    elif lang=='fr':
        return('bonjour')
    else:
        return('Hello')

userLang = input('| es | fr | en | : ')
name = input ('Enter your name here: ')
print()
print(greet(userLang), name)