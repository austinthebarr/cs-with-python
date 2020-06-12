def selectionSort(L):
    suffix = 0
    
    while suffix != len(L):
        for i in range(suffix,len(L)):
            if L[i] < L[suffix]:
                L[i], L[suffix] = L[suffix], L[i]
        suffix += 1
    return L
    
    
selectionSort([1,7,2,5,8])
