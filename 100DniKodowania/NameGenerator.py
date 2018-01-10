import random
female_name=['Kasia','Basia','Asia']
male_name=['Bart','Charles','Kuba']
female_surname=['Adamowicz','Sufryd','Ostrowska']
male_surname=['Stoch','Malek','Starczyk']

choice=(input('Wybierz imie do wygenerowania: m-męskie, f-żeńskie: '))

while choice not in ['F','f','M','m']:
    choice=(input('Podales bledne imie. Wybierz imie do wygenerowania: M/m-męskie, F/f-żeńskie: '))
    
if(choice=='m' or 'M'):
    print(random.choice(male_name)+" "+random.choice(male_surname))
elif choice=='f' or 'F':
    print(random.choice(female_name)+" "+random.choice(female_surname))
