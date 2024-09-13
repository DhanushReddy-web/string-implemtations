import pytest
from string import StringPerformance  # Replace `your_module_name` with the actual module name

def test_palindrome():
    assert StringPerformance.palindrome("madam") is True
    assert StringPerformance.palindrome("hello") is False
    assert StringPerformance.palindrome("A man a plan a canal Panama".replace(" ", "").lower()) is True

def test_reverse():
    assert StringPerformance.reverse("hello") == "olleh"
    assert StringPerformance.reverse("world") == "dlrow"
    assert StringPerformance.reverse("") == ""

def test_factorial():
    assert StringPerformance.factorial(5) == 120
    assert StringPerformance.factorial(0) == 1
    assert StringPerformance.factorial(1) == 1

def test_largest():
    assert StringPerformance.largest([1, 3, 2, 5, 4]) == 5
    assert StringPerformance.largest([-10, -3, -1, -7]) == -1
    assert StringPerformance.largest([1.5, 2.5, 3.5]) == 3.5

def test_count_frequency():
    assert StringPerformance.count_frequency([1, 1, 2, 3, 3, 3]) == {1: 2, 2: 1, 3: 3}
    assert StringPerformance.count_frequency([5, 5, 5, 5]) == {5: 4}
    assert StringPerformance.count_frequency([]) == {}

def test_is_prime():
    assert StringPerformance.is_prime(2) is True
    assert StringPerformance.is_prime(17) is True
    assert StringPerformance.is_prime(4) is False
    assert StringPerformance.is_prime(1) is False

def test_find_common_elements():
    assert StringPerformance.find_common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert StringPerformance.find_common_elements(["apple", "banana"], ["banana", "cherry"]) == ["banana"]
    assert StringPerformance.find_common_elements([], [1, 2, 3]) == []

def test_bubble_sort():
    elements = [3, 2, 1]
    StringPerformance.bubble_sort(elements)
    assert elements == [1, 2, 3]

    elements = [5, 4, 3, 2, 1]
    StringPerformance.bubble_sort(elements)
    assert elements == [1, 2, 3, 4, 5]

def test_find_second_largest():
    assert StringPerformance.find_second_largest([1, 2, 3, 4, 5]) == 4
    assert StringPerformance.find_second_largest([10, 10, 9, 8, 8, 7]) == 9
    assert StringPerformance.find_second_largest([1]) is None

def test_remove_duplicates():
    assert StringPerformance.remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert StringPerformance.remove_duplicates([5, 5, 5, 5]) == [5]
    assert StringPerformance.remove_duplicates([]) == []
