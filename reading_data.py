import pandas as pd

df = pd.read_csv('fake_data.csv')
print(df)

number_of_row = len(df)

for i in range(0, number_of_row):
    for column in df.columns:
        print(column)
        print(df.loc[i, column])

