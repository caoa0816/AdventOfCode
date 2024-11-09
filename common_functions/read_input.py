def read_input_file(filename='day1_input.txt'):
    input_file = f'./2023/2023_input'
    with open (f'{input_file}/{filename}') as file:
        contents = file.read()
        return contents.strip().split('\n')