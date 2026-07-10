# if = თუ
# else = სხვა შემთხვევაში
# elif = სხვა შემთხვევაში თუ
# if, else და elif არის პირობითი ოპერატორები, რომლებიც საშუალებას გვაძლევს შევამოწმოთ გარკვეული პირობა და კოდის შესრულება ამ პირობის მიხედვით.
age = int(input("Enter your age: "))


permission = input("Do you have a doctor's permission? (yes/no): ")

if age >= 18 and permission == "yes":
    print("ვარჯიშზე დაშვება ნებადართულია!")
else:
    print("სავარჯიშოდ გჭირდებათ სრულწლოვანება და ექიმის ნებართვა")




for x in range(1, 11):

    y = x ** 2


    if y > 30:
        print(f"რიცხვი {x}-ის კვადრატია {y} და ის მეტია 30-ზე")




correct_password = "12345"


while True:
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("correct password")
        break
    else:
        print("incorrect password")