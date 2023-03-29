def pairSum(list, sum):
    length = len(list)
    pair_count = 0
    for i in range(length):
        for j in range(i + 1, length):
            if list[i] + list[j] == sum:
                pair_count += 1
    return pair_count


# print(pairSum([2, 8, 10, 5, -2, 5], 10))
