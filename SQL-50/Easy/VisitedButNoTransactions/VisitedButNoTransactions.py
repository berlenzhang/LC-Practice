import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, how='left', on='visit_id')
    df = df[df['transaction_id'].isnull()]
    df = df.groupby('customer_id', as_index=False)['visit_id'].count()
    df = df.rename(columns={'visit_id': 'count_no_trans'})
    return df