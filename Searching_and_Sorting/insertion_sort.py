def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        j = i - 1
        temp = list[i]
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp

    return list


# ========================================================
# ========================================================


def my_new_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]

    return list


print(insertion_sort([6, 7, 3, 0, -1, 8, 2, 9, 11, 90, 37, 1]))
