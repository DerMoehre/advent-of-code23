import pandas as pd

test_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
# read in data as txt file
file = open("input.txt", "r")
data = file.read()
input = data.split('\n')

def numbers(input):
    result = 0
    for number in input:
        digit = ''.join(x for x in number if x.isdigit())
        if len(digit) > 2:
            new_digit = digit[0] + digit[-1]
            result += int(new_digit)
        elif len(digit) == 1:
            new_digit = int(digit) * 11
            result += int(new_digit)
        else:
            result += int(digit)
    return result

print(numbers(input))