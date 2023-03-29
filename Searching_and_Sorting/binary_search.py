# =========================
#   My Implementation more optimized than online solns --> tried optimizing the binary search
#   So far I have run through many testcases
# =========================


def search_ele(list, ele):
    start = 0
    end = len(list) - 1
    # loop_count = 0
    while start < end:
        mid = (start + end) // 2
        if list[end] < ele or list[start] > ele:
            return -1
        if list[start] == ele:
            return start
        if list[mid] == ele:
            return mid
        if list[end] == ele:
            return end
        if list[mid] < ele:
            start = mid + 1
        if list[mid] > ele:
            end = mid - 1
        # loop_count += 1
    # print(f"loop_count: {loop_count}")
    return -1


# =========================
#   Refactored(Traditional Way) but i guess mine is faster at time compelexity
# =========================


def search_ele(list, ele):
    start = 0
    end = len(list) - 1
    # loop_count = 0
    while start <= end:
        mid = (start + end) // 2
        if list[mid] < ele:
            start = mid + 1
        elif list[mid] > ele:
            end = mid - 1
        else:
            return mid
        # loop_count += 1
    # print(f"loop_count: {loop_count}")
    return -1


print(search_ele([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 9))  # -1
print(search_ele([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 0))  # 0
print(search_ele([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 16))  # 8
print(search_ele([1, 2, 4, 7, 8, 12, 15, 19, 24, 50, 69, 80, 100], 16))  # -1
print(search_ele([1, 2, 4, 7, 8, 12, 15, 19, 24, 50, 69, 80, 100], 69))  # 10
print(search_ele([1, 2, 4, 7, 8, 12, 15, 19, 24, 50, 69, 80, 100], 12))  # 5
print(search_ele([1, 3, 7, 9, 11, 12, 45], 11))  # 4
print(search_ele([1, 3, 7, 9, 11, 12, 45], 1))  # 0
print(search_ele([1, 3, 7, 9, 11, 12, 45], 2))  # -1
print(search_ele([1, 3, 7, 9, 11, 12, 45], 80))  # -1
print(search_ele([1, 3, 7, 9, 11, 12, 45], 12))  # 5
print(search_ele([1, 2, 3, 4, 5, 6], 9))  # -1
print(search_ele([1, 2, 3, 4, 5, 6], 6))  # 5




# 1 3 7 9 11 12 45  # --> 9 -> mid= 3 -> arr[mid] == 9 --> return mid

# ===================
# ===================

# 1 3 7 9 11 12 45  # --> 11 -> mid= 3 -> arr[mid] == 11 --> 9 < 11 -> start = mid + 1 --> arr[start] == 11 -> return start

# ===================
# ===================

# 1 3 7 9 11 12 45  # --> 7 -> mid = 3 -> arr[mid] == 7 -> 9 > 7 -> end = mid - 1 ->
