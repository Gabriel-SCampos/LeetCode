import pytest
import pandas as pd
from problems.easy.combine_two_tables_175.solution import combine_two_tables  # Replace with the actual import

@pytest.fixture
def input_data():
    person = [
        {"personId": 1, "lastName": "Wang", "firstName": "Allen"},
        {"personId": 2, "lastName": "Alice", "firstName": "Bob"}
    ]
    address = [
        {"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"},
        {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}
    ]
    return person, address

def test_combine_two_tables(input_data):
    # Transform input data into dataframes
    person, address = input_data
    person = pd.DataFrame(person)
    address = pd.DataFrame(address)

    # Transform expected output into a dataframe
    expected_output = pd.DataFrame([
        {"firstName": "Allen", "lastName": "Wang", "city": None, "state": None},
        {"firstName": "Bob", "lastName": "Alice", "city": "New York City", "state": "New York"}
    ])

    # Call the function and assert the result
    result = combine_two_tables(person, address)
    pd.testing.assert_frame_equal(result, expected_output, check_dtype=False)
