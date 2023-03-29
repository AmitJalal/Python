def tripletSum(list, target):
    tripletSum = 0
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if list[i] + list[j] + list[k] == target:
                    tripletSum += 1
    return tripletSum


# print(tripletSum([1, 2, 3, 4, 5, 6, 7], 12))  #5
