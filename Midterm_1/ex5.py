birthdays = {"Ana": "01/17/1991", "Marija": "02/17/1991", "Stefan": "03/17/1991", "Aleksandar": "03/17/1991"}
print("Welcome to the birthday dictionary. We know the birthdays of:")
for birthday in birthdays:
    print(birthday)
print("Which birthday would you like to be displayed?")
birthday_search = input()
if birthday_search not in birthdays:
    print("Sorry, we do not have the birthday of " + birthday_search)
else:
    print("The birthday of " + birthday_search + " is on " + birthdays[birthday_search])
