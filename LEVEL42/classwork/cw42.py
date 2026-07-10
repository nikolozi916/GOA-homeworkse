# upper() ადიდებს ჩვენს მიერ პრინტში დაწერილ სიტყვას მაგ:
print("nikolozi".upper())


# lower() აპატარავებს ჩვენს მიერ პრინტში დაწერილ სიტყვას მაგ:
print("ANDRIA".lower())


# capitalize() მხოლოდ პირველ ასოს ადიდებს მაგ:
print("giorgi".capitalize())


# find()ეძებს იმ ასოსო რომელსაც დავწერთ ფრჩხილებში მაგ:
print("giorgi".find("g"))


# დოტ ნოტაცია იგივე წერტილოვანი ნოტაცია,არის პროგრამირებაში ფართოდ გავრცელებული სინტაქსური წესი.
def make_upper(text):

    upper_text = text.upper()

    print(upper_text)

make_upper("hello, world!")