operators = ("+", "-", "*", "**", "/", "//", "%")

print("Enter first operand:")
operand_1 = float(input())
print("Enter operatorot:")
operator = input()
print("Enter second operand:")
operand_2 = float(input())

if operator not in operators:
    print("Unknown operator!")
if operator == "/" or operator == "//" and operand_2 == 0:
    print("Division with zero is not allowed!")
else:
    if operator == "+":
        print("Result: " + str(operand_1 + operand_2))
    if operator == "-":
        print("Result: " + str(operand_1 - operand_2))
    if operator == "*":
        print("Result: " + str(operand_1 * operand_2))
    if operator == "**":
        print("Result: " + str(operand_1 ** operand_2))
    if operator == "/":
        print("Result: " + str(operand_1 / operand_2))
    if operator == "//":
        print("Result: " + str(operand_1 // operand_2))
    if operator == "%":
        print("Result: " + str(operand_1 % operand_2))
