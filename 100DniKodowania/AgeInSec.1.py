import datetime

yourYear=int(input('Give your year: '))
yourMonth=int(input('Give your month: '))
yourDay=int(input('Give your day: '))

yourDate=datetime.datetime(yourYear,yourMonth,yourDay)

currentDate=datetime.datetime.today()
daysDifference=currentDate-yourDate
print(daysDifference)

secondsDifference=daysDifference.total_seconds()
print('%.2f seconds are from your Birthday date till today. %d' % (secondsDifference, 2))