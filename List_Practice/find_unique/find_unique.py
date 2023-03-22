def unique(s, li):
    for i in range(s):
        j = 0
        while j < s:
            if i != j:
                if li[i] == li[j]:
                    break
            j += 1
        if j == s:
            return li[i]
    else:
        return -1


test_cases = int(input())
while test_cases:
    size = int(input())
    list = [int(x) for x in input().split()]
    print(unique(size, list))
    test_cases -= 1
