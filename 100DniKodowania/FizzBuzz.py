liczbaPodzielnaPrzez3="Fizz"
liczbaPodzielnaPrzez5="Buzz"
liczbaPodzielnaPrzez15="FizzBuzz"

for cyfra in range(0,101):
    if cyfra%15==0:
        print(liczbaPodzielnaPrzez15)
        continue
    if cyfra%3==0:
        print(liczbaPodzielnaPrzez3)
        continue
    if cyfra%5==0:
        print(liczbaPodzielnaPrzez5)
        continue
    print (cyfra)

