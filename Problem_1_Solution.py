def main():
    preferences = specify_preferences()
    if preferences[1] == 1:
        print(encode_string(preferences))
    else:
        print(decode_string(preferences))


def specify_preferences():
    preference = int(input("Please specify function: \n"
                           "\"1\" to encode\n"
                           "\"2\" to decode\n\n>>> "))
    if preference == 2:
        string = (input("Enter string to decode: ").lower(), preference)
        return string
    if preference == 1:
        string = (input("Enter string to encode: "), preference)
        return string


def encode_string(string):
    old_string = string[0]
    new_string = ""
    temp_str = ""
    previous_letter = old_string[0]
    repeat_count = 0
    index = 0


    for y in old_string:
        if y == previous_letter:
            repeat_count += 1
            index += 1
            previous_letter = y
            if index == len(old_string):
                temp_str += str(repeat_count) + previous_letter.upper()

        if y != previous_letter:
            new_string += str(repeat_count) + previous_letter.upper()
            repeat_count = 1
            index += 1
            previous_letter = y
            if index == len(old_string):
                temp_str += str(repeat_count) + previous_letter.upper()

    new_string += temp_str
    return new_string


def decode_string(string):
    old_string = string[0].upper()
    new_string = ""
    temp_str = ""
    temp_str2 = ""
    temp = ""

    for y in old_string:
        if y.isnumeric():
            temp_str += y
            temp_str2 += y
        else:
            number = int(temp_str2)
            temp_str2 = ""
            for x in range(number):
                new_string += y.upper()
    return new_string


main()