# 1)
age = int(input("Enter your age: "))

if age >= 18:
    print("you are adult.")
else:
    print("you are minor.")




# 2)
word = input("Enter any word: ")

for char in word:
    print(char)




# 3)
for i in range(1, 16):
    if i % 3 == 0:
        print(i)
