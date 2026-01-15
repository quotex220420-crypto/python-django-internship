# Number Analyzer using for loop

for number in range(1, 21):
    if number == 13:
        continue

    if number % 2 == 0:
        print(number, "- Even")
    else:
        print(number, "- Odd")
