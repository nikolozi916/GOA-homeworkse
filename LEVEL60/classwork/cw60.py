#1)
def accum(st):
    result = []
    for i, c in enumerate(st):
        part = c.upper() + (c.lower() * i)
        result.append(part)
    return "-".join(result)



#2)
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result


#3)
def count_sheep(n):
    result = []
    for i in range(1, n + 1):
        result.append(f"{i} sheep...")
    return "".join(result)
