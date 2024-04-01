import datetime

print("Enter the name and years:")
name_and_years = input()
name = name_and_years.split()[0]
years = name_and_years.split()[1]
current_year = datetime.date.today().year
years_to_add = 100 - int(years)
hundred_years_old = current_year + years_to_add
print(name+" will be 100 years old in "+str(hundred_years_old))
