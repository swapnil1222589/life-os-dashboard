import pandas as pd

def summarize_day(df):
    return df.groupby("Category")["Minutes_Used"].sum().to_string()
