import pytest
from problems.easy.minimum_operations_to_make_array_values_equal_to_K_3375.solution import Solution
@pytest.fixture
def solution():
    return Solution()

def test_minimum_operations_case_1(solution):
    assert solution.minOperations([5, 2, 5, 4, 5], 2) == 2

def test_minimum_operations_case_2(solution):
    assert solution.minOperations([2, 1, 2], 2) == -1

def test_minimum_operations_case_3(solution):
    assert solution.minOperations([9, 7, 5, 3], 1) == 4

def test_minimum_operations_case_4(solution):
    assert solution.minOperations([1, 1, 1, 1], 1) == 0

def test_minimum_operations_case_5(solution):
    assert solution.minOperations([10, 20, 30], 15) == -1

def test_minimum_operations_case_6(solution):
    assert solution.minOperations([100, 200, 300], 100) == 2
