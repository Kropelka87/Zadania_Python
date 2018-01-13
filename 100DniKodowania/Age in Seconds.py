import datetime
import inflect #converting numbers to words
userDate=''

while True:
  userDate=input("Please input your birth date in format YYYY-MM-DD:")
  try:
    birthDate=datetime.datetime.strptime(userDate,'%Y-%m-%d')
    difference=(datetime.datetime.now()-birthDate).total_seconds()
    p=inflect.engine()
    print("You are %d seconds old." % difference)
    print("Let's spell it: %s seconds. Wow!" % p.number_to_words(int(difference)))
    if difference <0:
      print("You are from the future!")
    break
  except:
    print("Incorrect date format or incorrect date!")
  