print("Enter numbers:")
numbers = []
number = int(input())
while number != "end":
    numbers.append(number)
    number=input()
new_numbers = [numbers[0], numbers[-1]]
print("The first number is: " + str(new_numbers[0]) + ", and the last number is: " + str(new_numbers[1]))
