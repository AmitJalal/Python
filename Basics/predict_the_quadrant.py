test_cases = int(input())
count = 0
while count < test_cases:
    # x, y = [int(x) for x in input().split()]
    x, y = map(int, input().split())
    if x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if y > 0:
            print("Q2")
        else:
            print("Q3")
    count = count + 1
