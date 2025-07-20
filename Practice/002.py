# Initialize max_value to a very small number to ensure any valid input is greater
max_value = float('-inf')

print("Please enter five numbers:")

# Loop five times to get input and find the maximum
for i in range(5):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            break  # Exit the inner loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if num > max_value:
        max_value = num

print("The maximum value entered is: {max_value}")