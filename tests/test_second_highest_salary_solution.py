import pytest
import pandas as pd
from problems.medium.second_highest_salary_176.solution import second_highest_salary

@pytest.fixture
def example_1_data():
    employee = [
        {"id": 1, "salary": 100},
        {"id": 2, "salary": 200},
        {"id": 3, "salary": 300}
    ]
    return pd.DataFrame(employee)

@pytest.fixture
def example_2_data():
    employee = [
        {"id": 1, "salary": 100}
    ]
    return pd.DataFrame(employee)

@pytest.fixture
def example_3_data():
    employee = [
        {"id": 1, "salary": 300},
        {"id": 2, "salary": 300},
        {"id": 3, "salary": 200},
        {"id": 4, "salary": 100}
    ]
    return pd.DataFrame(employee)

@pytest.fixture
def example_4_data():
    employee = [
        {"id": 1, "salary": 300},
        {"id": 2, "salary": 300}
    ]
    return pd.DataFrame(employee)

def test_second_highest_salary_example_1(example_1_data):
    result = second_highest_salary(example_1_data)
    expected = pd.DataFrame([{"SecondHighestSalary": 200}])
    pd.testing.assert_frame_equal(result, expected)

def test_second_highest_salary_example_2(example_2_data):
    result = second_highest_salary(example_2_data)
    expected = pd.DataFrame([{"SecondHighestSalary": None}])
    pd.testing.assert_frame_equal(result, expected)

def test_second_highest_salary_example_3(example_3_data):
    result = second_highest_salary(example_3_data)
    expected = pd.DataFrame([{"SecondHighestSalary": 200}])
    pd.testing.assert_frame_equal(result, expected)

def test_second_highest_salary_example_4(example_4_data):
    result = second_highest_salary(example_4_data)
    expected = pd.DataFrame([{"SecondHighestSalary": None}])
    pd.testing.assert_frame_equal(result, expected)