Favourite_language = {
    "Anderson": "c",
    "Favour": "Python",
    "Miracle": "Java",
    "Sir_Nobs": "Django",
}

'''for name, language in Favourite_language.items():
    print(f'\nname', {name})
    print(f'language', {language})
    print(f"{name.title()}'s favourite language is {language.title()}.")'''

friends = ['Miracle', 'Sir_Nobs']
for name in Favourite_language.keys():
    print(name.title())
    
    if name in friends:
        language = Favourite_language[name].title()
        print(f"  Hi {name.title()} I see you love {language}\n")
    if 'Zim' not in Favourite_language:
        print('Zim please take the pool')