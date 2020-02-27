def max_val(t):
 """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
        max_val((5, (1,2), [[1],[2]])) returns 5.
        max_val((5, (1,2), [[1],[9]])) returns 9.""" 
  m = 0
  for v in range(len(t)):
    if type(t[v]) is int:
        if m < t[v]:
            m = t[v]
    else:
        rec = max_val(t[v])
        if m < rec:
            m = rec
  return m
  
