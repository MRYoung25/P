data = [1, 3, 4, 6, 8, 7, 2, 5, 10, 11, 9, 13, 12]
def SelectSort(L):
    length = len(L)
    if length == 0 or length == 1:
        return L

    def min(s):
        smallest = s
        for i in range(s, length):
            if L[i] < L[smallest]:
                smallest = i
        return smallest

    for i in range(length):
        smallest = min(i)
        if i != smallest:
            temp = L[smallest]
            L[smallest] = L[i]
            L[i] = temp
    return L
pass

print SelectSort(data)
