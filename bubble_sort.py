def bubbleSort(L):
    swap = False
    while not swap:
        swap = True
        for i in range(1,len(L)):
            if L[i-1] > L[i]:
                swap = False
                L[i], L[i-1] = L[i-1], L[i]
          
    return L
                
bubbleSort([7,4,2,10, 63, 1])

