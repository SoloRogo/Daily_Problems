def main():
    print(analyze_string(input("Enter string to analyze: ")))


def analyze_string(string):

    # assigning_values
    rc_inverse = "("
    ro_inverse = ")"
    cc_inverse = "{"
    co_inverse = "}"
    sc_inverse = "["
    so_inverse = "]"
    index = 1
    temp_list = [string[0]]
    ideal_char = False

    # checking_for_invalid_characters
    for y in string:
        if y != "(" and y != ")" and y != "{" and y != "}" and y != "[" and y != "]":
            return "Not a valid string"

    # storing_first_ideal_character
    # learn_dictionaries_from_sean
    if string[0] == "(":
        ideal_char = ro_inverse
    if string[0] == ")":
        ideal_char = rc_inverse
    if string[0] == "{":
        ideal_char = co_inverse
    if string[0] == "}":
        ideal_char = cc_inverse
    if string[0] == "[":
        ideal_char = so_inverse
    if string[0] == "]":
        ideal_char = sc_inverse

    # making_sure_string_is_even
    if len(string) % 2 == 0:

        for i in range(1, len(string)):
            x = string[i]
            index += 1
            print(temp_list)

            # checking_if_last_character_win
            if x == ideal_char and index == len(string):
                return "Balanced"

            # checking_if_last_character_fail
            if x != ideal_char and index == len(string):
                return "Not Balanced"

            # if_not_last_character...

            # ...and_match
            if x == ideal_char:
                if temp_list:
                    del temp_list[len(temp_list) - 1]
                if len(temp_list) > 0:
                    if temp_list[len(temp_list) - 1] == "(":
                        ideal_char = ro_inverse
                    if temp_list[len(temp_list) - 1] == ")":
                        ideal_char = rc_inverse
                    if temp_list[len(temp_list) - 1] == "{":
                        ideal_char = co_inverse
                    if temp_list[len(temp_list) - 1] == "}":
                        ideal_char = cc_inverse
                    if temp_list[len(temp_list) - 1] == "[":
                        ideal_char = so_inverse
                    if temp_list[len(temp_list) - 1] == "]":
                        ideal_char = sc_inverse
                continue

            # ...and_not_a_match
            if x != ideal_char:
                temp_list.append(x)

                if x == "(":
                    ideal_char = ro_inverse
                    continue
                if x == ")":
                    return "Not Balanced"
                if x == "{":
                    ideal_char = co_inverse
                    continue
                if x == "}":
                    return "Not Balanced"
                if x == "[":
                    ideal_char = so_inverse
                    continue
                if x == "]":
                    return "Not Balanced"
            else:
                return "Not a valid string"
    else:
        return "Not balanced"

    return "Balanced"


main()
