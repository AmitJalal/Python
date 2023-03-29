# ==================================
#    --->  log(N)
# ==================================

def sort_zero_one(list):
    start = 0
    end = len(list) - 1
    while start <= end:
        if list[start] == list[end]:
            if list[start] == 0:
                start += 1
            if list[start] == 1:
                end -= 1
        elif list[start] < list[end]:
            start += 1
            end -= 1
        elif list[start] > list[end]:
            list[start], list[end] = list[end], list[start]
            start += 1
            end -= 1

    return list

# =============================
#         -->  O(N)
# =============================

def sort_zero_one(list):
    zeroPos = 0
    current = 0
    while current < len(list):
        if list[current] == 0:
            list[current], list[zeroPos] = list[zeroPos], list[current]
            zeroPos = zeroPos + 1
        current = current + 1

    return list


# 1 0 1 1 0 1 0 1
print(sort_zero_one([1, 0, 1, 1, 0, 1, 0, 1]))  # [0, 0, 0, 1, 1, 1, 1, 1]

print(sort_zero_one([0, 1, 1, 0, 1, 0, 1]))  # [0, 0, 0, 1, 1, 1, 1]
