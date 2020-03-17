def greet(lang):
    if lang=='es':
        return('Hola')
    elif lang=='fr':
        return('Bonjour')
    elif lang=='polski':
        return('Jak sie masz')
    else:
        return('Hello')

userLang = input('| es | fr | polski | en | : ')
name = input ('Enter your name here: ')
print()
print(greet(userLang), name)