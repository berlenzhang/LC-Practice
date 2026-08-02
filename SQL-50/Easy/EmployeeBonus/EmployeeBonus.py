import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(bonus, how='left', on='empId')
    merged = merged[(merged['bonus'].isnull()) | (merged['bonus'] < 1000)]
    result = merged[['name', 'bonus']]
    return result