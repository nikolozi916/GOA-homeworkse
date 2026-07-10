score = int(input("Enter student score (0-100): "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


number = float(input("Enter number: "))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First Number is Greater than second one")
else:
    print("Second Number is Greater than first one")




num = int(input("Enter number: "))

if num % 2 == 0:
    print("number is even")
else:
    print("number is Odd")



temp = float(input("Enter the temperature in Celsius.: "))

if temp < 0:
    print("Cold ❄️")
elif 0 <= temp <= 30:
    print("Normal 🌤️")
else:
    print("Hot ☀️")