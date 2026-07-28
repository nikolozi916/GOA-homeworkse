# first classwork codewars.
def monkey_count(n):
    return list(range(1, n + 1))

# second.
def filter_list(l):
    return [x for x in l if not isinstance(x, str)]
    

# third. 
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')