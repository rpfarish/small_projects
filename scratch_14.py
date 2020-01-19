# have person guess a number and if they are right than let them enter their
# name and tell them they are superman
num = 0
gender = input("Enter your gender: Man or Woman: \n")
gender.lower()
print("Enter a number between 0 and 30")
while num != 27:
    try:
        num = abs(int(input("Enter a Number: ")))
    except ValueError:
        print("Please Enter A Number.")

if gender == 'woman':
    def name (super_hero):
        result1 = "is Superwoman"
        print(super_hero)
        return result1

    print("Enter your name:")
    print(name(input("") + "\n"))
else:
    def name (super_hero):
        result1 = "is Superman"
        print(super_hero)
        return result1

    print("Enter your name:")
    print(name(input("") + "\n"))





