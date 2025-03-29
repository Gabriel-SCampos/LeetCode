from solution import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_longest_palindrome_example(solution):
    assert solution.longestPalindrome("abccccdd") == 7

def test_longest_palindrome_single_character(solution):
    assert solution.longestPalindrome("a") == 1

def test_longest_palindrome_empty_string(solution):
    assert solution.longestPalindrome("") == 0

def test_longest_palindrome_all_unique(solution):
    assert solution.longestPalindrome("abcdef") == 1

def test_longest_palindrome_all_even(solution):
    assert solution.longestPalindrome("aabbcc") == 6

def test_longest_palindrome_mixed(solution):
    assert solution.longestPalindrome("aaabbbccc") == 7

def test_longest_palindrome_repeated_characters(solution):
    assert solution.longestPalindrome("aaaa") == 4

def test_longest_palindrome_case_sensitivity(solution):
    assert solution.longestPalindrome("AaBbCc") == 1
