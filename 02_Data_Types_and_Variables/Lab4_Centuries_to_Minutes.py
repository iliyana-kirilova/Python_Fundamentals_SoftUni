DAYS_IN_YEAR = 365.2422
century = int(input())

years = century*100
days = int(years * DAYS_IN_YEAR)
hours = days * 24
minutes = hours * 60

print(f'{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')