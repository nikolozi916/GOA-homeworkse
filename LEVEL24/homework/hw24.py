number = int(input("Enter a number: "))

if number % 2 == 0:
    print ('Even')
else:
    print ('odd')






number = float(input("Enter a number"))

if number > 0:
    print ('it is positive')
else:
    print ('it is negative')




age = int(input("Enter your age"))

if age >= 18:
    print ('you can vote')
else:
    print ('you are still small')




score = int(input("Enter the score: "))

if score >= 50:
    print("Passed")
else:
    print("You failled")




password = "1234"
user_input = input("Enter password: ")

if user_input == password:
    print("correct")
else:
    print("Wrong password")