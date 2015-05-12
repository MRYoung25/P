data = [1, 3, 4, 6, 8, 7, 2, 5, 10, 11, 9, 13, 12]
def SelectSort(L):
    length = len(L)
    if length == 0 or length == 1:
        return L
    
    for i in range(length):
        smallest = i
        for j in range(i+1, length):
            if L[j] < L[smallest]:
                smallest = j
        (L[smallest], L[i]) = (L[i], L[smallest])
    return L
pass

print SelectSort(data)
