
Interactive Calculator & Unit Converter
Internship Project
"""

def basic_calculator():
    print("\n--- Basic Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %, ^): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        elif op == "^":
            result = num1 ** num2
        else:
            print("Invalid operator entered.")
            return

        print(f"Result: {num1} {op} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Length (Kilometers <-> Miles)")
    print("2. Weight (Kilograms <-> Pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")

    choice = input("Select conversion type (1-3): ").strip()

    try:
        if choice == "1":
            print("a. Kilometers to Miles\nb. Miles to Kilometers")
            sub = input("Choose (a/b): ").strip().lower()
            val = float(input("Enter value: "))
            if sub == "a":
                print(f"{val} km = {val * 0.621371:.2f} miles")
            elif sub == "b":
                print(f"{val} miles = {val / 0.621371:.2f} km")
            else:
                print("Invalid option.")

        elif choice == "2":
            print("a. Kilograms to Pounds\nb. Pounds to Kilograms")
            sub = input("Choose (a/b): ").strip().lower()
            val = float(input("Enter value: "))
            if sub == "a":
                print(f"{val} kg = {val * 2.20462:.2f} lbs")
            elif sub == "b":
                print(f"{val} lbs = {val / 2.20462:.2f} kg")
            else:
                print("Invalid option.")

        elif choice == "3":
            print("a. Celsius to Fahrenheit\nb. Fahrenheit to Celsius")
            sub = input("Choose (a/b): ").strip().lower()
            val = float(input("Enter value: "))
            if sub == "a":
                print(f"{val}°C = {(val * 9/5) + 32:.2f}°F")
            elif sub == "b":
                print(f"{val}°F = {(val - 32) * 5/9:.2f}°C")
            else:
                print("Invalid option.")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Invalid input! Please enter a numerical value.")


def main():
    while True:
        print("\n============================================")
        print("  INTERACTIVE CALCULATOR & UNIT CONVERTER   ")
        print("============================================")
        print("1. Use Calculator")
        print("2. Use Unit Converter")
        print("3. Exit")

        selection = input("Choose an option (1-3): ").strip()

        if selection == "1":
            basic_calculator()
        elif selection == "2":
            unit_converter()
        elif selection == "3":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid selection, please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()