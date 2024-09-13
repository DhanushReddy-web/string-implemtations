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
    print("Press 1 to check palindrome of a string")
    print("Press 2 to do reverse opeartion")
    print("Press 3 to exit the menu")

    choice = input("Enter [1/2/3] from the menu: ")

    if choice == '1':
        word = input("Enter the string to check for palindrome: ")
        if StringOperations.palindrome(word):
            print(f"The entered string {word} is palindrome")
        else:
            print(f"The entered string {word} is not a palindrome")

    elif choice == '2':
        word = input("Enter the string to reverse:")
        print("The reversed string is ", StringOperations.reverse(word))

    elif choice == '3':
        print("Thank you for exploring string operations")
    else:
        print("Invalid Values , try again!!!")

if __name__ =="__main__":
    main()



