class StringImplementations:
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

    choice = input("Enter your choice[1/2/3] :")

    if choice == '1':
        word = input("Enter a string to check for palindrome:  ")
        if StringImplementations.palindrome(word):
            print(f"The entered string {word} is palindrome")
        else:
            print(f"The entered string {word} is not palindrome")


    elif choice == '2':
        word = input("Enter a string to reverse:")
        #reversed_word = StringImplementations.reverse(word)
        print(f"The entered string after reverse is",StringImplementations.reverse(word))



    elif choice == '3':
        print("Thank you for using pycharm")


    else:
        print("Invalid values try again")


if __name__ == "__main__":
    main()
