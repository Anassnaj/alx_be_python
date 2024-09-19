# pattern_drawing.py

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))

    # Ensure the size is positive
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Draw the pattern using a while loop for rows
    row = 0
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    main()
