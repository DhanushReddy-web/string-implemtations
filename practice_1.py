class StringOperations:
    @staticmethod
    def palindrome(string):
        reversed_string = string[::-1]
        return string == reversed_string

    @staticmethod
    def reverse(string):
        return string[::-1]


def main():
    print("String Operations Menu:")
    print("1. Check if a string is a palindrome")
    print("2. Reverse a string")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        word = input("Enter a string to check for palindrome: ")
        if StringOperations.palindrome(word):
            print(f"The string '{word}' is a palindrome.")
        else:
            print(f"The string '{word}' is not a palindrome.")

    elif choice == '2':
        word = input("Enter a string to reverse: ")
        reversed_word = StringOperations.reverse(word)
        print(f"The reversed string is: '{reversed_word}'")

    elif choice == '3':
        print("Thank you for using String Operations. Goodbye!")

    else:
        print("Invalid choice. Please run the program again and enter 1, 2, or 3.")


if __name__ == "__main__":
    main()