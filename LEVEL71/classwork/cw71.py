#1) codewars:
def multiply(*nums):
    total = 1
    for n in nums:
        total *= n
    return total

#2) codewars:
def even_or_odd(number):
    for i in [number]:
        if i % 2 == 0:
            return "Even"
        else:
            return "Odd"


#3) codewars:
def make_negative(number):
    for i in range(1):          
        if number > 0:
            return - number
    return number


#4)
def solution(nums):
    if nums is None:
        return []
    result = list(nums)
    n = len(result)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


#5)
def number_to_string(num):
    return str(num)


#6)
def get_count(sentence):
    return len([c for c in sentence if c in "aeiou"])

def get_count(sentence):
    return sum(sentence.count(v) for v in "aeiou")

#7)
def solution(number):
    if number <= 0:
        return 0
    
    total = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total



#8)
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total


#9)
def repeat_str(repeat, string):
    result = ''
    for i in range(repeat):
        result += string
    return result



#10)
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string_:
        if char not in vowels:
            result += char
    return result


#11)
def high_and_low(numbers):
    nums = []
    current_num = ""
    for char in numbers:
        if char == " ":
            if current_num:
                nums.append(int(current_num))
                current_num = ""
        else:
            current_num += char
    if current_num:
        nums.append(int(current_num))
    highest = nums[0]
    lowest = nums[0]
    
    for num in nums:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    return str(highest) + " " + str(lowest)



#12)
def friend(x):
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return friends



#13)
def longest(a1, a2):
    seen = set()
    for char in a1 + a2:
        seen.add(char)
    return ''.join(sorted(seen))



#14)


#15)

