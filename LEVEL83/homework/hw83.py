#1)
def pig_it(text):
    words = []
    word = ""

    for ch in text:
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    result = ""
    for i in range(len(words)):
        w = words[i]
        if len(w) == 1 and w in "!?.,:;":
            new_w = w
        else:
            new_w = w[1:] + w[0] + "ay"

        if i == 0:
            result += new_w
        else:
            result += " " + new_w



#2)
def generate_hashtag(s):
    words = []
    word = ""

    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    if len(words) == 0:
        return False

    hashtag = "#"
    for w in words:
        first_char = w[0].upper()
        rest_chars = w[1:].lower()
        hashtag += first_char + rest_chars

    if len(hashtag) > 140:
        return False

    return hashtag



#3)
def create_phone_number(n):
    phone = "("
    for i in range(len(n)):
        phone += str(n[i])
        if i == 2:
            phone += ") "
        elif i == 5:
            phone += "-"
    return phone

#4)
def duplicate_count(text):
    lower_text = ""
    for ch in text:
        lower_text += ch.lower()

    counts = {}
    for ch in lower_text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    duplicates = 0
    for key in counts:
        if counts[key] > 1:
            duplicates += 1

    return duplicates

#5)
def solution(number):
    if number < 0:
        return 0

    total = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total += num

    return total