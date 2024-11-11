from common_functions.read_input import read_input_file


LETTER_TO_DIGIT = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight":"8", "nine":"9"
    }


def extract_numbers_from_document(calibration_value):
    numerical_values = [char for char in calibration_value if char.isdigit()]
    return numerical_values


def extract_first_and_last_digit(numerical_values: str):
    relevant_digits = int(numerical_values[0] + numerical_values[-1])
    return relevant_digits


def calculate_sum_of_all_digits(digits: list):
    return sum(digits)


def transform_letter_to_digit(calibration_value):
    transformed_calibration_value = ""
    
    for i in range(0, len(calibration_value)):
        if calibration_value[i].isdigit():
            transformed_calibration_value += calibration_value[i]
            i += 1
        else:
            for j in range(i+3, i+6):
                if calibration_value[i:j] in list(LETTER_TO_DIGIT.keys()):
                     transformed_calibration_value += LETTER_TO_DIGIT[calibration_value[i:j]]
                     i += len(calibration_value[i:j])
                     j += len(calibration_value[i:j])
            
    return transformed_calibration_value


if __name__ == "__main__":
    calibration_document = read_input_file()
    
    first_and_last_digit_pt1, first_and_last_digit_pt2 = [], []
    for content in calibration_document:
        digits_from_doc_pt1 = extract_numbers_from_document(content)
        relevant_digits_pt1 = extract_first_and_last_digit(digits_from_doc_pt1)
        first_and_last_digit_pt1.append(relevant_digits_pt1)

        converted_value = transform_letter_to_digit(content)
        relevant_digits_pt2 = extract_first_and_last_digit(converted_value)
        first_and_last_digit_pt2.append(relevant_digits_pt2)

    print(calculate_sum_of_all_digits(first_and_last_digit_pt1))
    print(calculate_sum_of_all_digits(first_and_last_digit_pt2))
    
    

    # txt = "jdklghtbz1eightrhvfmnlknlghg77"
    # print(transform_letter_to_digit(txt))