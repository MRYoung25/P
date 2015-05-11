def SelectSort(L):
    assert(type(L) == type(['']))
    length = len(L)
    if length == 0 or length == 1:
        return L

    def max(s):
        largest = s
        for i in xrange(s, length):
            if L[i] > L[largest]:
                largest = i
        return largest

    for i in xrange(length):
        largest = max(i)
        if i != largest:
            temp = L[largest]
            L[largest] = L[i]
            L[i] = temp
    return L
pass

print SelectSort(date)
