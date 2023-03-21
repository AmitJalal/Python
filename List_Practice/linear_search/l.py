def find_index(elem, lst):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    else:
        return -1


def process_test_case(elem, lst):
    """Process a single test case and return the index of elem in lst, or -1 if not found"""
    return find_index(elem, lst)


def read_input_file(filename):
    """Read an input file and return a list of test cases"""
    with open(filename, "r") as file:
        test_cases = []
        while True:
            # Read the element to be found
            elem_line = file.readline().strip()  
            if not elem_line:  # End of file
                break
            # Element to be found in the current test case
            elem = int(elem_line)
            # Read the list of integers
            lst = list(map(int, file.readline().split()))
            test_cases.append((elem, lst))
    return test_cases


if __name__ == "__main__":
    filename = "test.txt"
    test_cases = read_input_file(filename)
    for i, (elem, lst) in enumerate(test_cases):
        index = process_test_case(elem, lst)
        print(f"Test case {i+1}: Index of {elem} = {index}")
