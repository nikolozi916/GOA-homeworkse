#1) codewars:1
def solution(string):
    return string[::-1]


#2)
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle - 1 : middle + 1]
    else:
        return s[middle]


#3)
def solution(number):
    if number < 0:
        return 0
    
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
            
    return total_sum
