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


# with open('test.txt', 'r') as file:
#     while True:
#         n_line = file.readline().strip()  # Read the next line
#         if not n_line:  # End of file
#             break
#         n = int(n_line)  # Number of elements in the current test case
#         lst = list(map(int, file.readline().split()))[:n]  # Read the list of integers
#         max_elem = max(lst)  # Find the maximum element in the list
#         print("Maximum element:", max_elem)


# with open('test.txt', 'r') as file:
#     n = int(file.readline())  # Read the number of elements
#     lst = list(map(int, file.readline().split()))  # Read the list of integers
# max_elem = max(lst)  # Find the maximum element in the list
# print("Maximum element:", max_elem)


# def user_input():
#     with open("test.txt", "r") as readfile:
#         input = readfile.read()
#         lines = input.split("\n")
#         for line in lines:
#             li.append(line)


# li = []

# user_input()
# print(li)


# def execute_user_input():
#     with open("test.txt") as file:
#         while True:
#             line1 = file.readline().strip()
#             line2 = file.readline().strip()

#             if not line2:
#                 break

#             result = fun(line1, line2)
#             print(result)

# execute_user_input()

# def fun(len, list):
#     print(len, list)
