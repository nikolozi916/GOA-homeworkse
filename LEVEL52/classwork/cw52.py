# first classwork codewars:
def minimum(arr):

    return min(arr)
def maximum(arr):
    return max(arr)

# second.
def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False


# third.
def find_short(s):
    words = s.split()
    shortest_length = len(words[0])
    
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
            
    return shortest_length




# fourth.
def row_sum_odd_numbers(n):
    start_value = n * (n - 1) + 1
    row_sum = 0
    for i in range(n):
        row_sum += start_value + (i * 2)
    return row_sum


# fifth.
def odd_or_even(arr):
    total = 0
    for num in arr:
        total += num
        
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
