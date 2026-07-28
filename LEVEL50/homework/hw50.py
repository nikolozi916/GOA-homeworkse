# first homework codewars:
 function sumOfPositives(arr) 
  return arr.reduce((sum, num) => num > 0 ? sum + num : sum, 0);





# second.
def repeat_str(n, s):
    return s * n




# third.
def remove_char(s):
    return s[1:-1]



# fourth.
def square_sum(numbers):
    return sum(x**2 for x in numbers)



# fifth.
def find_smallest_int(arr):
    return min(arr)



# sixth
def summation(num):
    return num * (num + 1) // 2



# seventh
def count_sheeps(sheep):
    return sum(1 for s in sheep if s)


# eighth
def no_space(x):
    return x.replace(" ", "")



# ninth
def litres(time):
    return int(time * 0.5)



# tenth
def century(year):
    return (year + 99) // 100
