#Complete the read_file() function to read in the "sampletext.txt" file using the open function and return the entire contents of the file.
def read_file(file_name):
    with open(file_name) as file:
        sample = file.read()
        print(sample)
        return sample


#Complete the read_file_into_line() function so that it returns a data structure of all the contents of the file in a line-by-line sequential order.
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        sample = file.readlines()
        print(sample)
        return sample


#Fill in the write_first_line_to_file() that accepts two arguments. This should write only the first line of the file contents into the given output file.
def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    try:
        with open(output_filename, 'w') as file:
            file.write(first_line)
    except Exception as e:
        print('Error: ', e)
        return


#Complete the read_even_numbered_lines() to return a list of the even-numbered lines of a file (2, 4, 6, etc.)
def read_even_numbered_lines(file_name):
    with open(file_name) as file:
        sample = file.readlines()
        even_lines = []
        for index, line in enumerate(sample):
            if (index + 1) %2 == 0:
                even_lines.append(line)
    return even_lines


#Fill in the read_file_in_reverse() function to return a list of the lines of a file in reverse order.
def read_file_in_reverse(file_name):
    reverse_lines =[]
    with open(file_name) as file:
        sample = file.readlines()
        for line in sample:
            reverse_lines.insert(0, line)
    print(reverse_lines)
    return reverse_lines