1)
number = float(input("Enter number: "))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is Negative")



2)
sales = [45, 50, 62, 40, 55, 90, 105]

# პირველი ელემენტი (ორშაბათი)
print(sales[0])

# მესამე ელემენტი (ოთხშაბათი)
print(sales[2])

# ბოლო ელემენტი უარყოფითი ინდექსით (კვირა)
print(sales[-1])

# მნიშვნელობის შეცვლა (ხუთშაბათი არის მე-4 ელემენტი, ინდექსი 3)
sales[3] = 48
print(sales)



3)
ratings = [8.5, 7.2, 9.0, 6.8, 9.5]

# მეორე ფილმი (ინდექსი 1)
print(ratings[1])

# მეოთხე ფილმი (ინდექსი 3)
print(ratings[3])

# ბოლო ფილმი უარყოფითი ინდექსით
print(ratings[-1])

# მესამე ფილმის (ინდექსი 2) განახლება და სიის დაბეჭდვა
ratings[2] = 9.3
print(ratings)