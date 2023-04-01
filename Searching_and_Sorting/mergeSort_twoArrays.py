def mergeSortTwoArrays(arr1, arr2):
    mergeSortedArr = []
    len1 = len(arr1)
    len2 = len(arr2)
    i = 0
    j = 0

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            mergeSortedArr.append(arr1[i])
            i += 1
        else:
            mergeSortedArr.append(arr2[j])
            j += 1

    while i < len1:
        mergeSortedArr.append(arr1[i])
        i += 1

    while j < len2:
        mergeSortedArr.append(arr2[j])
        j += 1

    return mergeSortedArr


list1 = [2, 7, 34, 45, 48, 100, 248, 260, 300, 327, 366, 370]
list2 = [0, 1, 5, 9, 13, 74, 88, 108, 140, 400]
print(mergeSortTwoArrays(list1, list2))
