imie1=input('Podaj pierwsze imię: ')
imie2=input('Podaj drugie imię: ')
imie1=imie1.lower()
imie2=imie2.lower()
samogloski=['a','e','i','o','u','y']

count=0
iloscSamoglosekA=0
iloscSamoglosekB=0
if (imie1[0] and imie2[0]) in samogloski:
  count+=10
  print(count)
if imie1[0]==imie2[0]:
  count+=20
  print(count)
if (imie1[0] and imie2[0]) not in samogloski:
  count+=5
  print(count)
for i in samogloski:
  iloscSamoglosekA+=imie1.count(i)
  iloscSamoglosekB+=imie2.count(i)
  
iloscSpolglosekA=len(imie1)-iloscSamoglosekA
iloscSpolglosekB=len(imie2)-iloscSamoglosekB

if iloscSamoglosekA==iloscSamoglosekB:
  count+=12
  print(count)
if iloscSpolglosekA==iloscSpolglosekB:
  count+=12
  print(count)
  
lista=['i','o','v','e']

for i in lista:
  if (imie1.count(i)>0 and imie2.count(i)>0):
    count+=7
print(count)
