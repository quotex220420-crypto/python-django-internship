# Find first multiple of 7 between 1 and 50

for number in range(1, 51):
    if number % 7 == 0:
        print("First multiple of 7 is:", number)
        break
