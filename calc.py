def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Division")

    choice = input("Enter your choice (1 or 2): ")
    
    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    
    if choice == "1":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == "2":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division is: {result}")

calculator()
