# Python program to sort numbers from arguments or use default array

import sys

# Default array
default_numbers = [5, 2, 9, 1, 7]

print(default_numbers)

# Check if arguments are provided
if len(sys.argv) > 1:
    try:
        # Convert arguments to integers
        numbers = [int(num) for num in sys.argv[1:]]
        print("Array from arguments:", numbers)
    except ValueError:
        print("Error: All arguments must be integers.")
        sys.exit(1)
else:
    # Use default array
    numbers = default_numbers
    print("Using default array:", numbers)

# Sort the array
numbers.sort()

# Print sorted array
print("Sorted array:", numbers)
