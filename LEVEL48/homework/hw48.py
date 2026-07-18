# first homework: CODEWARS.
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)



# second.
def words_to_marks(s):
    return sum(ord(char) - 96 for char in s)


# third.
def remove_smallest(numbers):
    
    if not numbers:
        return []
    
    result = numbers.copy()
    
    result.remove(min(result))

    return result


# fourth.
def duplicate_encode(word):
   
    word_lower = word.lower()
    
    
    return "".join(")" if word_lower.count(char) > 1 else "(" for char in word_lower)



# fifth.
def create_phone_number(n):
   
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)