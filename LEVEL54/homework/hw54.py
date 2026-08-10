#1
def find_average(numbers):
    
    if not numbers:
        return 0
    
    
    return sum(numbers) / len(numbers)
#2
def words_to_marks(s):
    return sum(ord(char) - 96 for char in s)
#3
def remove_smallest(numbers):
    
    if not numbers:
        return []
    
    
    min_index = numbers.index(min(numbers))
    
    
    return numbers[:min_index] + numbers[min_index + 1:]
#4
def duplicate_encode(word):
    
    word = word.lower()
    
    
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    
    
    result = []
    for char in word:
        if counts[char] == 1:
            result.append("(")
        else:
            result.append(")")
    
    return "".join(result)
#5
def create_phone_number(n):
    
    digits = "".join(str(num) for num in n)
    
    
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"