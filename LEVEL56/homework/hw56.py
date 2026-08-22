def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def repeat_str(n, s):
    return s * n

def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

def find_smallest_int(arr):
    return min(arr)

def sum_of_a_series(n):
    return n * (n + 1) // 2


def mumbling(s):
    return "-".join(
        char.upper() + char.lower() * i
        for i, char in enumerate(s)
    )

def reverse_string(s):
    return s[::-1]


def counting_sheep(sheep):
    return sheep.count(True)

def solution(n, multiples):
    total = 0
    # გავიაროთ რიცხვები 0-დან n-1-მდე
    for i in range(n):
        # შევამოწმოთ, იყოფა თუ არა `i` მასივის რომელიმე ელემენტზე
        if any(i % m == 0 for m in multiples if m != 0):
            total += i
    return total


