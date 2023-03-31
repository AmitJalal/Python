def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(length - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        length -= 1
    return list


# ==========================================================================
# ===========================================================================


def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(length - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


# ==========================================================================
# ==========================================================================


print(bubble_sort([7, 4, 0, 5, 1, 2, 3, 0, -9]))
