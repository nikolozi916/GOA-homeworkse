# first classwork: CODEWARS.
def get_middle(s):

    index = len(s) // 2
    if len(s) % 2 == 0:
        return s[index - 1 : index + 1]
    return s[index]

# SECOND.
def maskify(cc):

    return '#' * (len(cc) - 4) + cc[-4:]


# THIRD.
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


# FOURTH.
def check_exam(arr1, arr2):
    score = 0


    for key, ans in zip(arr1, arr2):
        if ans == "":
            score += 0
        elif key == ans:
            score += 4
        else:
            score -= 1


    return max(0, score)

# FIFTH.
def monkey_count(n):
    return list(range(1, n + 1))