import pandas as pd
from faker import Faker

# create the fake data using faker
fake = Faker()
profiles = [fake.profile() for i in range(10)]

# store the fake profile data with pandas
df = pd.DataFrame(profiles)
df = df[['name', 'mail', 'address']]

# create the phone number and comment fake data
numbers = [fake.phone_number() for i in range(0,10)]
comment = '-'

#store the data at the dataframe 
df['phone number'] = numbers
df['comments'] = comment

#change the column name
df.rename(columns={'name': 'Name', 'mail':'Email', 'address':'Address'}, inplace=True)

# export the data to CSV
df.to_csv('fake_data.csv', index=False)