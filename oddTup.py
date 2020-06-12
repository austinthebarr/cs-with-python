L = [1, 1, 1, 1, 4]
n = 2

def getSublists(L, n):
   megaList = []
   while len(L) > 0:
       if len(L[:n]) < (n // 2):
         sub = sub[:(n // 2)] + L[:n]
       else:
           sub = L[:n]
           megaList.append(sub)
           del L[:n]
   return megaList
       

print(getSublists(L, n))
            