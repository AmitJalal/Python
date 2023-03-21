def find_max_ele(n, lst):
    """Process a single test case and return the maximum element"""
    return max(lst)


def read_input_file(filename):
    """Read an input file and return a list of test cases"""
    with open(filename, "r") as file:
        test_cases = []
        while True:
            n_line = file.readline().strip()  # Read the next line
            if not n_line:  # End of file
                break
            n = int(n_line)  # Number of elements in the current test case
            lst = list(map(int, file.readline().split()))[
                :n
            ]  # Read the list of integers
            test_cases.append((n, lst))
    return test_cases


if __name__ == "__main__":
    filename = "test.txt"
    test_cases = read_input_file(filename)
    for i, (n, lst) in enumerate(test_cases):
        max_elem = find_max_ele(n, lst)
        print(f"Test case {i+1}: Maximum element = {max_elem}")