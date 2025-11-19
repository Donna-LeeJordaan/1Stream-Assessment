import unittest
from solution import reverse_string, is_palindrome, bubble_sort


class TestSolution(unittest.TestCase):
    
    def test_reverse_string(self):
        # Normal case
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        
        # Edge cases
        self.assertEqual(reverse_string(""), "")  # Empty string
        self.assertEqual(reverse_string("a"), "a")  # Single character
        self.assertEqual(reverse_string("12345"), "54321")  # Numbers
    
    def test_is_palindrome(self):
        # Normal cases - palindromes
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Madam"))
        
        # Normal cases - not palindromes
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("race a car"))
        
        # Edge cases
        self.assertTrue(is_palindrome(""))  # Empty string
        self.assertTrue(is_palindrome("a"))  # Single character
        self.assertTrue(is_palindrome("12321"))  # Numbers only
    
    def test_bubble_sort(self):
        # Normal case
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(bubble_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        
        # Edge cases
        self.assertEqual(bubble_sort([]), [])  # Empty list
        self.assertEqual(bubble_sort([1]), [1])  # Single element
        self.assertEqual(bubble_sort([5, 5, 5, 5]), [5, 5, 5, 5])  # All same elements
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted


if __name__ == '__main__':
    unittest.main()
