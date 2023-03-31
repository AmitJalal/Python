def pushZeroToEnd(list):
    length = len(list)
    endPushNum = 0
    for i in range(1, length):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] == endPushNum:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp

    return list


# ==================================
#    --> BETTER APPROACH:
# ==================================


def pushZeroToEnd(list):
    indexWithoutZero = 0
    endPushNum = 0
    for i in range(len(list)):
        if list[i] != endPushNum:
            list[indexWithoutZero], list[i] = list[i], list[indexWithoutZero]
            indexWithoutZero += 1
    return list


print(pushZeroToEnd([0, 2, 0, 1, 0, 0, 4, 3, 2, 0]))
