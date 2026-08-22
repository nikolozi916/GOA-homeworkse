def find_sum(n):
    
    return sum(range(100, 100 * (n + 1), 100))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def reverse_words(text):
    return " ".join(text.split()[::-1])

def duplicate_encode(word):
    word = word.lower()
    count = {}
    
    for char in word:
        count[char] = count.get(char, 0) + 1
    
    
    result = ""
    for char in word:
        if count[char] > 1:
            result += ")"
        else:
            result += "("
            
    return result


def compose(*funcs):
    def composed_function(x):
        
        
        for func in reversed(funcs):
            x = func(x)
        return x
    return composed_function

