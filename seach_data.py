import pandas as pd

def search_by_id():
    try:
        df = pd.read_csv("sampleData-1.csv")
        search_id = input("Enter ID to search: ").strip()
        if search_id.isdigit():
            result = df[df['ID'] == int(search_id)]
            if not result.empty:
                print("\nSearch Result:\n", result)
            else:
                print("No record found with that ID.")
        else:
            print("Invalid input. Please enter a numeric ID.")
    except FileNotFoundError:
        print("CSV file not found. Please save data first.")
