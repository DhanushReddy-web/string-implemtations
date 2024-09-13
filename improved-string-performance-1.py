import math
from typing import List, Dict, Union

class StringPerformance:
    @staticmethod
    def palindrome(string: str) -> bool:
        return string == string[::-1]

    @staticmethod
    def reverse(string: str) -> str:
        return string[::-1]

    @staticmethod
    def factorial(n: int) -> int:
        return math.factorial(n)

    @staticmethod
    def largest(numbers: List[Union[int, float]]) -> Union[int, float]:
        return max(numbers)

    @staticmethod
    def count_frequency(numbers: List[Union[int, float]]) -> Dict[Union[int, float], int]:
        return {num: numbers.count(num) for num in set(numbers)}

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        return all(number % i != 0 for i in range(2, int(number**0.5) + 1))

    @staticmethod
    def find_common_elements(list1: List, list2: List) -> List:
        return list(set(list1) & set(list2))

    @staticmethod
    def bubble_sort(elements: List[Union[int, float]]) -> None:
        n = len(elements)
        for i in range(n):
            for j in range(0, n - i - 1):
                if elements[j] > elements[j + 1]:
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]

    @staticmethod
    def find_second_largest(numbers: List[Union[int, float]]) -> Union[int, float, None]:
        unique = list(set(numbers))
        if len(unique) < 2:
            return None
        return sorted(unique)[-2]

    @staticmethod
    def remove_duplicates(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
        return list(dict.fromkeys(numbers))

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float_list_input(prompt: str) -> List[float]:
    while True:
        try:
            return [float(x) for x in input(prompt).split()]
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

def main():
    menu_options = {
        1: ("Palindrome check", lambda: print(StringPerformance.palindrome(input("Enter a string: ")))),
        2: ("Reverse string", lambda: print(StringPerformance.reverse(input("Enter a string: ")))),
        3: ("Factorial", lambda: print(StringPerformance.factorial(get_int_input("Enter a number: ")))),
        4: ("Find largest number", lambda: print(StringPerformance.largest(get_float_list_input("Enter numbers separated by spaces: ")))),
        5: ("Count frequency", lambda: print(StringPerformance.count_frequency(get_float_list_input("Enter numbers separated by spaces: ")))),
        6: ("Check prime", lambda: print(StringPerformance.is_prime(get_int_input("Enter a number: ")))),
        7: ("Find common elements", lambda: print(StringPerformance.find_common_elements(
            input("Enter first list elements separated by spaces: ").split(),
            input("Enter second list elements separated by spaces: ").split()
        ))),
        8: ("Bubble sort", lambda: print(StringPerformance.bubble_sort(get_float_list_input("Enter numbers to sort: ")))),
        9: ("Find second largest", lambda: print(StringPerformance.find_second_largest(get_float_list_input("Enter numbers separated by spaces: ")))),
        10: ("Remove duplicates", lambda: print(StringPerformance.remove_duplicates(get_float_list_input("Enter numbers separated by spaces: ")))),
        11: ("Exit", lambda: print("Thank you for using String Performance"))
    }

    while True:
        print("\n*** String Performance Menu ***")
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")

        choice = get_int_input("Enter your choice (1-11): ")
        
        if choice in menu_options:
            menu_options[choice][1]()
            if choice == 11:
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
