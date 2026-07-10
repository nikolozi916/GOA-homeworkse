# 1)
number = 15
if number > 10:
    print("more than 10")
else:
    print("less than 10")



# 2)
user_num = int(input("Enter number: "))
if user_num == 15:
    print("equal to 15")
else:
    print("not equal to 15")



# 3)
text = input("Enter text: ")
if text == "group84":
    print("you are correct")
else:
    print("you are wrong")



# 4)
for i in range(50, 101, 5):
    print(i)



# 5)
full_name = "ნიკოლოზ მუშკუდიანი"
for char in full_name:
    print(char)



# 6)
i = 20
while i <= 50:
    print(i)
    i += 1



# 7)
# For loop
for i in range(100):
    print(i)

# While loop
i = 0
while i < 100:
    print(i)
    i += 1



# 8)
# for loop
for i in range(101):
    print(i)

# While loop
i = 0
while i <= 100:
    print(i)
    i += 1


# 9)
# For loop
for i in range(10, 21):
    print(i)

# While loop
i = 10
while i <= 20:
    print(i)
    i += 1


# 10)
# For loop
for i in range(100, 201, 5):
    print(i)

# While loop
i = 100
while i <= 200:
    print(i)
    i += 5

# 11)
# For loop
for i in range(10, -1, -1):
    print(i)

# While loop
i = 10
while i >= 0:
    print(i)
    i -= 1


# 12)
num = float(input("Enter any number: "))

if num > 0:
    print("this number is Positive")
elif num < 0:
    print("This number is a negative number.")
else:
    print("this number is zero")


# 13)
age = int(input("Enter your age: "))
if age < 0:
    print("incorrect info")
elif age <= 12:
    print("you are child")
elif age <= 19:
    print("you are teen")
elif age <= 64:
    print("you are Adult")
elif age <= 120:
    print("You are old.")
else:
    print("Guru or magician")

# 14)
num = float(input("Enter any number: "))

if num > 0:
    print("this number is positive")
elif num < 0:
    print("this number is negative")
else:
    print("this number is zero")


# 15)
day = int(input("Enter number 1-7: "))

if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("I don't know what day it is ")


# 16)
num = float(input("Enter number: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2) 


# 17)
password = input("Enter password: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


# 18)
user_num = int(input("Enter whole number: "))
total_sum = 0

for i in range(1, user_num + 1):
    total_sum += i

print("number total is:", total_sum)