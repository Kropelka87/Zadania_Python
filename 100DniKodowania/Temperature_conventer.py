print('Program przelicza temperaturę z Fahrenheit na Celsjusze i odwrotnie.')
skala=input('Wybierz opcję przeliczania: F-z Fahrenheit na Celsjusza, C-z Celsjusza na Fahrenheit: ')

while skala not in ['F','C']:
    skala=input('Podałeś błędną odpowiedź. Wybierz opcję przeliczania: F-z Fahrenheit na Celsjusza, C-z Celsjusza na Fahrenheit.')

temperature=float(input('Podaj temperaturę do przeliczenia: '))

while (skala=='C' and temperature<-273.15):
    temperature=float(input('Nie ma takie temperatury. Podaj temperaturę do przeliczenia: '))

if skala=='F':
    Celsjusz=5/9*(temperature-32)
    print('%.2f F tj. %.2f stopni Celsjusza.' % (temperature, Celsjusz))

elif skala=='C':
    Fahrenheit=32+9/5*temperature
    print('%.2f C tj %.2f stopni Fahrenheit.' % (temperature, Fahrenheit))
    if (temperature>-273 and temperature<0):
        print('Temperatura jest poniżej 0.')
    elif temperature==100:
        print('Jest to temperatura wrzenia.')
    elif temperature==0:
        print('Temperatura zamarzania.')


