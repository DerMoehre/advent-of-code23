

# read in data as txt file
file = open("input.txt", "r")
data = file.read()
input = data.split('\n')

# --- PART ONE ---

test_input_one = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

def numbers_part_one(input):
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

print(numbers_part_one(input))

# --- PART TWO ---

test_input_two = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

number_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

def string_to_int(input, mapping):
    new_list = []
    for word in input:
        for key, item in mapping.items():
            word = word.replace(key, str(item))
        new_list.append(word)
    return numbers_part_one(new_list)

print(string_to_int(input, number_map))
#print(translate)
