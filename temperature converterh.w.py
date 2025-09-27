print("-" * 40)
print("-----Temperature Converter-----")
print("-" * 40)

print("Please select a conversion: ")
print("1. Celcius to Farenhiet")
print("2. Farenhiet to Celcius")
print("-" * 40)

choice = int(input("Enter your choice: "))
print("-" * 40)

if choice == 1:
    celcius = float(input("Enter the temperature in celcius: "))
    farenhiet = (celcius*9/5)+32
    print(f"The temperature in farenhiet is{farenhiet:0.2f}")

elif choice == 2:
    farenhiet = float(input("Enter the temperature in farenhiet: "))
    celcius = (farenhiet-32) * 5/9
    print(f"The temperature in celcius is {celcius: 0.2f}")

else:
    print("Invalid choice! Please select from 1 or 2.")
    print("-" * 40)