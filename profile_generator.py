#PERSONAL PROFILE CARD GENERATOR
name = input("enter your full name(first and last):")
age = int(input("enter your age:"))
hobby = input("enter your favorite hobby:")


parts = name.split()
initials = parts[0][0].upper()+"."+parts[1][0].upper()+"."

print("Name :",name.title())




print("initials :",initials)
print("Age :",age)
print("Born :",2026-age)
print("Hobby :",hobby.capitalize())
print("Long name?",len(name)>8)


