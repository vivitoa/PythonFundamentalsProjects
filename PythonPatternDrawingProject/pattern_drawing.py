from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

while True:
    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern and save it to the variable
    if choice == 1:  # Right-angled Triangle
        pattern = ""
        for i in range(1, rows + 1):
            pattern += "*" * i + "\n"
        print(Fore.RED + pattern)  # Print with color

    elif choice == 2:  # Square with Hollow Center
        pattern = ""
        pattern += "*" * size + "\n"
        for _ in range(size - 2):
            pattern += "*" + " " * (size - 2) + "*" + "\n"
        pattern += "*" * size + "\n"
        print(Fore.RED + pattern)  # Print with color

    elif choice == 3:  # Diamond
        pattern = ""
        for i in range(rows):
            for j in range(rows - i - 1):
                pattern += ' '
            for k in range(2 * i + 1):
                pattern += Fore.GREEN + '*'  # Add color to stars
            pattern += "\n"

        for i in range(rows - 1):
            for j in range(i + 1):
                pattern += ' '
            for k in range(2 * (rows - i - 1) - 1):
                pattern += Fore.GREEN + '*'  # Add color to stars
            pattern += "\n"

        print(pattern)  # Print with color

    elif choice == 4:  # Left-angled Triangle
        pattern = ""
        for i in range(rows, 0, -1):
            pattern += Fore.MAGENTA + "*" * i + "\n"  # Add color to the stars
        print(pattern)  # Print with color

    elif choice == 5:  # Hollow Square
        pattern = ""
        for i in range(size):
            if i == 0 or i == size - 1:
                pattern += Fore.BLUE + "*" * size + "\n"  # Add color to the border
            else:
                pattern += Fore.BLUE + "*" + " " * (size - 2) + "*" + "\n"  # Add color to the border
        print(pattern)  # Print with color

    elif choice == 6:  # Pyramid
        pattern = ""
        for i in range(rows):
            for j in range(rows - i - 1):
                pattern += ' '
            for k in range(2 * i + 1):
                pattern += Fore.LIGHTBLUE_EX + '*'  # Add color to the stars
            pattern += "\n"
        print(pattern)  # Print with color

    elif choice == 7:  # Reverse Pyramid
        pattern = ""
        for i in range(rows):
            for j in range(i + 1):
                pattern += ' '
            for k in range(2 * (rows - i - 1) - 1):
                pattern += Fore.RED + '*'  # Add color to the stars
            pattern += "\n"
        print(pattern)  # Print with color

    elif choice == 8:  # Rectangle with Hollow Center
        pattern = ""
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for i in range(height):
            if i == 0 or i == height - 1:
                pattern += Fore.YELLOW + "*" * width + "\n"  # Add color to the border
            else:
                pattern += Fore.YELLOW + "*" + " " * (width - 2) + "*" + "\n"  # Add color to the border
        print(pattern)  # Print with color

    else:
        print(Fore.RED + "❌ Invalid choice! Please restart the program.")

    # Step 5: Ask if the user wants to save the pattern to a file
    save_choice = input(Fore.GREEN + "\nDo you want to save the pattern to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        with open("pattern.txt", "w") as file:
            file.write(pattern)
        print(Fore.GREEN + "✅ Pattern saved to 'pattern.txt'.")

    # Step 6: Optional - Allow the user to restart or exit
    restart = input("\nDo you want to restart the program? (yes/no): ").strip().lower()
    if restart != "yes":
        print("👋 Goodbye! Thank you for using the Python Pattern Drawing Program!")
        break  # Exit the loop and end the program
