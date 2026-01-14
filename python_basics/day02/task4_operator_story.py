num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nArithmetic Operations:")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("\nComparison Result:")
if num1 > num2:
    print("First number is greater than second number.")
elif num1 < num2:
    print("Second number is greater than first number.")
else:
    print("Both numbers are equal.")

print("\nLogical Decision:")
if num1 > 0 and num2 > 0:
    print("Both numbers are positive. Good choice!")
else:
    print("At least one number is not positive.")
