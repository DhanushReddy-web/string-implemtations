from math import factorial


class StringPerformance:
    @staticmethod
    def palindrome(string):
        reversed_string = string[::-1]
        return string == reversed_string

    @staticmethod
    def reverse(string):
        return string[::-1]

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    @staticmethod
    def largest(numbers):
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest

    @staticmethod
    def count_frequency(numbers):
        frequency = {}
        for num in numbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return frequency

    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def find_common_elements(list1,list2):
        common_elements =[]
        for item in list1:
            if item in list2:
                common_elements.append(item)
        return common_elements

    @staticmethod
    def bubble_sort(elements):
        n = len(elements)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if elements[j] > elements[j + 1]:
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]

    @staticmethod
    def find_second_largest(numbers):
        largest = float('-inf')
        second_largest = float('-inf')
        for num in numbers:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest

    @staticmethod
    def remove_duplicates(numbers):
        unique_numbers = []
        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        return unique_numbers



def main():
    print("***String Performance Menu*** ")
    print("Enter 1 to perform palindrome operation:")
    print("Enter 2 to perform reverse operation:")
    print("Enter 3 to perform factorial operation:")
    print("Enter 4 to find largest of the numbers:")
    print("Enter 5 to count frequency of numbers")
    print("Enter 6 to check if it is a  prime number")
    print("Enter 7 to find the common elements between two lists.")
    print("Enter 8 for bubble sort operation")
    print("Enter 9 to find second largest of a number")
    print("Enter 10 to remove duplicates from a list")
    print("Enter 11 to exit from menu:")

    choice = input("Enter either 1/2/3 to enter the menu: ")

    if choice == '1':
        word = input("Enter the string value to perform palindrome operation: ")
        if StringPerformance.palindrome(word):
            print(f"The entered string {word} is palindrome")
        else:
            print(f"The entered string {word} is not a palindrome")

    elif choice == '2':
        word = input("Enter the string value to perform reverse opeartion: ")
        print("The string value after reversal operation is:", StringPerformance.reverse(word))

    elif choice == '3':
        num = int(input("Enter a number to find the factorial: "))
        print(f"The factorial of {num} is ", StringPerformance.factorial(num))

    elif choice == '4':
        num = input("Enter the list of numbers: ")
        # num = [10, 20, 30, 100, 200, 2000]
        print("The largest number from the list is ", StringPerformance.largest(num))

    elif choice == '5':
        num = [1, 2, 3, 3, 2, 1, 2, 4, 3, 4, 5, 6, 7]
        print("The frequency count from the list is", StringPerformance.count_frequency(num))

    elif choice == '6':
        num = int(input("Enter a number to check if its prime: "))
        if StringPerformance.is_prime(num):
            print(f"The entered value {num} is a prime number")
        else:
            print(f"The entered value {num} is not a prime number")

    elif choice == '7':
        list_a = input("Enter list a elements")
        list_b = input("Enter list b elements")
        print(f"The common elements from a and b is ",StringPerformance.find_common_elements(list_a,list_b) )

    elif choice == '8':
        #nums = int(float((input("Enter the nums: "))))
        user_input = input("Enter the values to sort: ")
        nums = [int(x) for x in user_input.split()]
        StringPerformance.bubble_sort(nums)
        print(nums)


    elif choice == '9':
        # Test the function
        user_input = input("Enter numbers separated by spaces: ")
        try:
            nums = [float(x) for x in user_input.split()]
            second_largest_num = StringPerformance.find_second_largest(nums)
            print(f"The second largest number is: {second_largest_num}")
        except ValueError:
            print("Error: Please enter valid numbers separated by spaces.")

    elif choice == '10':
        user_input = input("Enter numbers separated by spaces: ")

        # Convert user input to a list of numbers
        try:
            nums = [int(x) for x in user_input.split()]
            unique_nums = StringPerformance.remove_duplicates(nums)
            print("Numbers with duplicates removed:", unique_nums)
        except ValueError:
            print("Error: Please enter valid integers separated by spaces.")

    elif choice == '11':
        print("Thank you for using String Performance")
    else:
        print("Invalid Values, Try again!!!")


if __name__ == "__main__":
    main()
