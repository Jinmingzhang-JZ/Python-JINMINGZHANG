import pandas as pd

def read_data_and_stats():
    try:
        df = pd.read_csv("sampleData-1.csv")
        print("\nData from sampleData-1.csv:\n")
        print(df)
        print("\nStatistics:\n")
        print(df.describe())
    except FileNotFoundError:
        print("File not found. Please save data first.")
