# ლოგიკური ოპერატორები გამოიყენება რამდენიმე პირობის ერთმანეთთან დასაკავშირებლად.
# for ციკლი გამოიყენება მაშინ, როცა წინასწარ ვიცით რამდენიჯერ უნდა გაეშვას კოდი ხოლო while ციკლი მუშაობს მანამ სანამ კონკრეტული პირობა არის ჭეშმარიტი (True).
Truename = "nikolozi"

while True:
    მომხმარებლისსახელი = input("please enter your name: ")

    if მომხმარებლის_სახელი == True_name:
        print("name is correct")
        break 
    else:
        print("name is incorrect")


My_list = ["Python", 25, True, 4.5]

del My_list[1] 

My_list.append("Goa Best")

# def  არის საკვანძო სიტყვა, რომლითაც ვქმნით  ფუნქციას.
def Personal_information(name, surname, age):
    print(f"გამარჯობა, მე ვარ {name} {surname} და ვარ {age} წლის.")