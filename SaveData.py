import pandas as pd

def save_data_to_csv():
    data = []
    print("Enter data rows. Format: ID,Weight,Age (type 'done' to finish)")
    while True:
        row = input(">>> ")
        if row.lower() == 'done':
            break
        try:
            parts = row.split(",")
            if len(parts) != 3:
                print("Invalid format. Please enter: ID,Weight,Age")
                continue
            id_, weight, age = int(parts[0]), float(parts[1]), int(parts[2])
            data.append([age])  # ONLY saving age, even though full input is used
        except ValueError:
            print("Invalid values. ID must be integer, Weight float, Age integer.")
    
    if data:
        df = pd.DataFrame(data, columns=["Age"])  # Only "Age" column in final CSV
        df.to_csv("sampleData-1.csv", index=False)
        print("Age data saved successfully to sampleData-1.csv")
    else:
        print("No data to save.")
