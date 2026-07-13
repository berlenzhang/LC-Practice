import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    shifted = weather.copy()
    shifted['recordDate'] = shifted['recordDate'] + pd.to_timedelta(1, unit='D')

    merged = pd.merge(weather, shifted, on='recordDate', suffixes=('_td', '_ytd'))
    res = merged[merged['temperature_td'] > merged['temperature_ytd']][['id_td']]
    res = res.rename(columns={'id_td': 'id'})
    return res