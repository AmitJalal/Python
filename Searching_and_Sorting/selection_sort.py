def sort(list):
    length = len(list)

    for i in range(length - 1):
        minIndex = i

        for j in range(i + 1, length):
            if list[j] < list[minIndex]:
                minIndex = j
                
        list[minIndex], list[i] = list[i], list[minIndex]

    return list


print(sort([0, 1, 5, 3, 0, 7, 2, 6, 0]))
