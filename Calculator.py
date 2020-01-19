

num1 = input("Please enter your first number: ")
opp = input("Please specify your operation type\n + - * or /: ")
num2 = input("Please enter your second number: ")
result = "Invalid"

if opp.lower() == "+":
    result = float(num1) + float(num2)
    print("Your result is: " + str(result))
elif opp.lower() == "-":
    result = float(num1) - float(num2)
    print("Your result is: " + str(result))
elif opp.lower() == "*":
    result = float(num1) * float(num2)
    print("Your result is: " + str(result))
elif opp.lower() == "/":
    result = float(num1) / float(num2)
    print("Your result is: " + str(result))
else:
    print("I'm sorry your input was invalid.\n Please restart the program.")
    quit()




