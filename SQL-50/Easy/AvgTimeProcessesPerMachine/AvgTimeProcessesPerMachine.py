import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_df = activity[activity['activity_type'] == 'start']
    end_df = activity[activity['activity_type'] == 'end']

    merged = end_df.merge(start_df, on=['machine_id', 'process_id'], suffixes=('_end', '_start'))
    merged['processing_time'] = merged['timestamp_end'] - merged['timestamp_start']
    merged = merged.groupby('machine_id', as_index=False)['processing_time'].mean()
    
    merged['processing_time'] = merged['processing_time'].round(3)
    return merged