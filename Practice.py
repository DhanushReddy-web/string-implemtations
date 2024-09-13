# # def reverse(string):
# #     string = string[::-1]
# #     return string
# #
# # s = "HPLAPTOP"
# # print("The original String is :",end="")
# # print(s)
# # print("The String after reverse is :",end="")
# # print(reverse(s))
#
# # def palindrome(string):
# #     reversed_string = string[::-1]
# #     return string == reversed_string
# #
# #
# # word = input("Enter The string:'")
# #
# # if palindrome(word):
# #     print(f"{word} is a palindrome")
# # else:
# #     print(f"{word} is not a palindrome")
#
# # def factorial(n):
# #     if n ==0:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
# #
# # number = 7
# # result = factorial(number)
# # print(f"The factorial of {number} is {result}")
#
# # def find_largest(numbers):
# #     largest = numbers[0]
# #     for num in numbers:
# #         if num > largest:
# #             largest = num
# #     return largest
# #
# # nums = [10,11,12,13,14,15,16]
# # largest = find_largest(nums)
# # print(f"The Largest no in the list is {largest}")
#
# # def cal_freq(numbers):
# #     freq = {}
# #     for num in numbers:
# #         if num in freq:
# #             freq[num] += 1
# #         else:
# #             freq[num] = 1
# #     return freq
# #
# # nums = [1,2,1,2,3,4,3,2,1,5]
# # count = cal_freq(nums)
# # print(count)
#
#
# def reverse(string):
#     string = string[::-1]
#     return string
#
#
# word = "Dhanush"
#
# print(f"The string before reversing is {word}")
# print(f"The string after reversing is ", reverse(word))
#
#
# def palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string
#
# word = "mommy"
#
# if palindrome(word):
#     print(f"The given string {word} is a palindrome")
# else:
#     print(f"The given string {word} is not a palindrome")
#
#

# def bubble_sort(elements):
#     n = len(elements)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if elements[j] > elements[j + 1]:
#                 elements[j], elements[j + 1] = elements[j + 1], elements[j]
#
# # Test the function
# nums = input("Enter the values to sort: ")
# bubble_sort(nums)
# print(nums)

def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]


# Get user input
user_input = input("Enter numbers separated by spaces: ")

# Convert user input into a list of integers
nums = [int(x) for x in user_input.split()]

# Sort the list
bubble_sort(nums)

# Print the sorted list
print("Sorted list:", nums)
