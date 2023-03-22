def reverse_list(list):
    length = len(list)
    for i in range(length//2):
        list[i], list[-i-1] = list[-i-1], list[i]
    return list

# ============================
# ============================

def reverseList(li):
    length = len(li)
    for i in range(length//2):
        li[i], li[length-i-1] = li[length-i-1], li[i]
    return li



li = [1, 2, 3, 4, 5, 6, 7]     
print(reverse_list(li))
print(reverseList(li))
