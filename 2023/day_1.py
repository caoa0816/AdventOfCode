# read doc line by line to extract all digits 

# extract the 1st & lst digit from each line, combine these two digit & convert to int 

# if len(digits) == 1, repeat it twice 

# sum of all int 

input_file = f'home/anna_cao/advent-of-code/2023/2023_input'

if __name__ == "__main__":
    with open (f"{input_file}/day1_input.txt") as file:
        contents = file.read()
        print(len(contents))
    

