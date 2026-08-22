def sum_even_numbers(seq):
    return sum(num for num in seq if num == int(num) and int(num) % 2 == 0)



def min_max(lst):
    return [min(lst), max(lst)]




def is_anagram(test, original):
    
    
    return sorted(test.lower()) == sorted(original.lower())


def remove_url_anchor(url):
    return url.split('#')[0]



def gimme(input_array):
    # Find the middle value by sorting a copy of the array
    middle_value = sorted(input_array)[1]
    
    # Return the index of that middle value in the original array
    return input_array.index(middle_value)