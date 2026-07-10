for i in range(0, 26, 2):
    print(i)



for i in range(26):
    if i % 2 == 0:
        print(i)
    else:
        continue


# პირობითი განცხადება არის if, else და elif. if ნიშნავს-თუ else-ნიშნავს სხვა შემთხვევაში ხოლო elif-ვიყენებთ მაშინ როდესაც პირობის სემოწმება გვინდა.
score = int(input("Enter score: "))

if score >= 90:
    print("you have A")
elif score >= 70:
    print("you have B")
elif score >= 50:
    print("you have C")
else:
    print("hold on")



password = "GOA BEST"
guess = input ("Enter password: ")

while guess != password:
    guess = input ("Enter password: ")

    if password == guess:
        print ("password is Correct")

    else:
        print ("password is incorrect")