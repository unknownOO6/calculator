# Task 2 - Calculator 🧮
# CodSoft Internship
# Written by a student who's learning Python and vibes 😄

def add(a, b):
    return a + b  # simple addition

def subtract(a, b):
    return a - b  # subtraction, obviously

def multiply(a, b):
    return a * b  # math stuff

def divide(a, b):
    if b == 0:
        print("Bro... you can't divide by zero 😭")
        return None
    return a / b

def get_number(text):
    # asking for number until user gets it right
    while True:
        try:
            num = float(input(text))
            return num
        except:
            print("That's not a number 😅 Try again.")

def main():
    print("====== My Mini Calculator 😎 ======")

    while True:
        print("\nWhat do you want to do?")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting... Bye bye 👋")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Umm... That's not a valid option 😬")
            continue

        # Get two numbers from the user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            sign = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            sign = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            sign = "*"
        elif choice == "4":
            result = divide(num1, num2)
            sign = "/"

        if result is not None:
            # I could've used f-strings but this feels old school
            print("Result: " + str(num1) + " " + sign + " " + str(num2) + " = " + str(result))

if __name__ == "__main__":
    main()
