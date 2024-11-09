from common_functions.read_input import read_input_file


def extract_numbers_from_document(calibration_document):
    numerical_values = []
    for content in calibration_document:
        numerical_value_by_line = [char for char in content if char.isdigit()]
        numerical_values.append(numerical_value_by_line)
    return numerical_values

def extract_first_and_last_digit(numerical_values: list):
    first_and_last_digits = []
    for digits in numerical_values:
        relevant_digits = int(digits[0] + digits[-1])
        first_and_last_digits.append(relevant_digits)
    return first_and_last_digits

def calculate_sum_of_all_digits(digits: list):
    return sum(digits)

if __name__ == "__main__":
    input = read_input_file()
    digits_from_doc = extract_numbers_from_document(input)
    first_and_last_digits = extract_first_and_last_digit(digits_from_doc)
    print(sum(first_and_last_digits))

    
