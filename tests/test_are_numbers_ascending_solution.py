from problems.easy.check_if_numbers_are_ascending_in_a_sentence_2042.solution import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_numbers_ascending_true(solution):
    assert solution.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") == True

def test_numbers_ascending_false(solution):
    assert solution.areNumbersAscending("hello world 5 x 5") == False

def test_numbers_ascending_mixed_case(solution):
    assert solution.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s") == False

def test_no_numbers(solution):
    assert solution.areNumbersAscending("this is a test sentence with no numbers") == True

def test_single_number(solution):
    assert solution.areNumbersAscending("there is only 1 number here") == True

def test_equal_numbers(solution):
    assert solution.areNumbersAscending("1 2 2 3") == False

def test_large_numbers(solution):
    assert solution.areNumbersAscending("10 20 30 40 50") == True

def test_mixed_text_and_numbers(solution):
    assert solution.areNumbersAscending("a 1 b 2 c 3 d 4") == True

def test_numbers_decreasing(solution):
    assert solution.areNumbersAscending("10 9 8 7 6") == False