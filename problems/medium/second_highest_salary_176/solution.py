import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_sorted_salaries = employee.sort_values(by='salary', ascending=False)['salary'].drop_duplicates()
    second_highest_salary = unique_sorted_salaries.iloc[1] if len(unique_sorted_salaries) > 1 else None
    return pd.DataFrame([{"SecondHighestSalary": second_highest_salary}])