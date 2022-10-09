"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()
length = len(numbers)
index = int(length/2)

if len(numbers) % 2 ==0:
    median = numbers[index] + numbers[index -1]
    median = median/2
else:
    median = numbers[index]
print(median)
