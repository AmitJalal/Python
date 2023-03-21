def life_span_macbook(list):
    sum = 0
    for ele in list:
        if ele > 0:
            sum += ele
    return sum


# # input
# # n = int(input())
# list = []
# for i in range(0, n):
#     list.append(int(input()))

# # output
# print(life_span_macbook(list))


def special_range(s, e):
    if e < 0 or (s > 0 and e < 0) or (s > 0 and e < s):
        print(-1)
        return

    if s < 0 and e >= 0:
        s = 0
    for i in range(s, e + 1):
        print(i)


# # input
# start = int(input())
# end = int(input())
# special_range(start, end)

# li = [1]
# li.insert(2,3)
# print(li[:2])


# =========================

# input with single line in python

li = [int(x) for x in input().split()]
print(li)

inp = list(map(int, input().split()))
print(inp)
