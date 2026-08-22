def is_isogram(string):

    clean_string = string.lower()
    
   
    return len(clean_string) == len(set(clean_string))



def xo(s):
    # Convert string to lowercase to handle case-insensitivity
    s = s.lower()
    
    # Count occurrences of 'x' and 'o'
    count_x = s.count('x')
    count_o = s.count('o')
    
    # Return True if counts are equal
    return count_x == count_o



def find_short(s):
    # Split the string into words by spaces
    words = s.split()
    
    # Find the minimum length of the words
    return min(len(word) for word in words)


def mumbling(s):
    result = []
    
    for i, char in enumerate(s):
        
        
        letter = char.lower()
        
        segment = letter.upper() + letter * i
        result.append(segment)
    
    
    return "-".join(result)




