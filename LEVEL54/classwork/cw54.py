# 1
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# 2
def max_diff(lst):
    
    if len(lst) <= 1:
        return 0
    
    
    max_val = max(lst)
    min_val = min(lst)
    
    
    return max_val - min_val

# 3 
def largest(n, xs):
    """Find the n highest elements in a list, returned in ascending order"""
    if n <= 0:
        return []
    if n >= len(xs):
        return sorted(xs)
    
    
    return sorted(sorted(xs, reverse=True)[:n])



# 4
def sum_even_numbers(seq): 
    return sum(x for x in seq if x % 2 == 0)

#5
def filter_list(l):
    return [x for x in l if isinstance(x, int) and not isinstance(x, bool)]