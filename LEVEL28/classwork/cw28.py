product_price = 50 
user_money = float(input("Enter how much money you have: ")) 

if user_money >= product_price:
    print("You can buy this product")
else:
    print("Not enough money")



number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")