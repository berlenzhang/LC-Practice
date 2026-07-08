import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]['author_id']
    df = df.drop_duplicates()
    df = df.sort_values()
    df = df.reset_index(drop=True)
    df = df.to_frame(name='id')
    return df