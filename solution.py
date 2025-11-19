def reverse_string(s: str) -> str:
    """
    Return the reversed version of the input string.
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring case and non-alphanumeric characters.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def bubble_sort(nums: list[int]) -> list[int]:
    """
    Sort a list of integers using bubble sort algorithm.
    """
    sorted_nums = nums.copy()
    n = len(sorted_nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
    return sorted_nums


if __name__ == "__main__":
    print("=== Function Examples ===")
    
    # Test reverse_string
    print("reverse_string('hello'):", reverse_string("hello"))
    print("reverse_string(''):", reverse_string(""))
    
    # Test is_palindrome
    test_str = "A man, a plan, a canal: Panama"
    print(f"is_palindrome('{test_str}'):", is_palindrome(test_str))
    print("is_palindrome('race a car'):", is_palindrome("race a car"))
    print("is_palindrome(''):", is_palindrome(""))
    
    # Test bubble_sort
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"bubble_sort({test_list}):", bubble_sort(test_list))
    print("bubble_sort([]):", bubble_sort([]))
