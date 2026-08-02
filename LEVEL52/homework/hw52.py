# first homework codewars:
def minimum(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

def maximum(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val





# second.
def solution(text, ending):
    if len(ending) > len(text):
        return False
        
    for i in range(1, len(ending) + 1):
        if text[-i] != ending[-i]:
            return False
            
    return True



# third.
def find_short(s):
    words = s.split()
    l = len(words[0])
    
    for word in words:
        if len(word) < l:
            l = len(word)
            
    return l



# fourth.
def row_sum_odd_numbers(n):
    start_num = n * (n - 1) + 1
    total_sum = 0
    
    for i in range(n):
        total_sum += start_num + (2 * i)
        
    return total_sum


# fifth.
def odd_or_even(arr):
    total_sum = 0
    
    for num in arr:
        total_sum += num
        
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"

