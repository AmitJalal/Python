def swapAlternate(n, arr):
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

n=int(input())
list = [int(x) for x in input().split()]

print(swapAlternate(n, list))







# def swapAlternate(n, arr):
#     for i in range(0, n - 1, 2):
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr


# def process_test_case(elem, lst):
#     return swapAlternate(elem, lst)


# def read_input_file(filename):
#     with open(filename, "r") as file:
#         file_input = []
#         total_test = int(file.readline().strip())

#         while total_test > 0:

#             while True:
#                 elem_line = file.readline().strip()
#                 if not elem_line:  
#                     break
#                 elem = int(elem_line)
#                 lst = list(map(int, file.readline().split()))
#                 file_input.append((elem, lst))

#             total_test -= 1

#     return file_input


# if __name__ == "__main__":
#     filename = "test.txt"
#     user_input = read_input_file(filename)
#     for i, (len, lst) in enumerate(user_input):
#         res = process_test_case(len, lst)
#         print(res)



