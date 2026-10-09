#1)
def solution(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


#2)
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


#3)
def make_negative(number):
    for num in [number]:
        if num > 0:
            return -num
        return num


#4)
def number_to_string(num):
    for x in [num]:
        return f"{x}"


#5)
def lovefunc(flower1, flower2):
    reminders = []
    for flower in [flower1, flower2]:
        reminders.append(flower % 2)
    return reminders[0] != reminders[1]
