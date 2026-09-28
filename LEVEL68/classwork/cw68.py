#1)
def get_count(sentence):
    vowels = set('aeiou')
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count


#2)
def to_jaden_case(string):
    words = string.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)


#3)
def largest(n, xs):
    """Find the n highest elements in a list"""
    if n <= 0:
        return []
    if n >= len(xs):
        return sorted(xs)
    top = []
    for x in xs:
        if len(top) < n:
            top.append(x)
        else: 
            min_val = min(top)
            if x > min_val:
                top[top.index(min_val)] = x
    return sorted(top)
k = 2
lst = [7, 6, 5, 4, 3, 2, 1]
print(largest(k, lst))


#4)
def two_oldest_ages(ages):
    oldest = second_oldest = float('-inf') 
    for age in ages:
        if age >= oldest:
            second_oldest = oldest  
            oldest = age
        elif age > second_oldest:
            second_oldest = age
    return [second_oldest, oldest]