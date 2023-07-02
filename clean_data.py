import pandas as pd

df = pd.read_csv('data.csv')

df['reviews'] = df['reviews'].apply(lambda x : int(x.replace('(', '').replace(')', '').replace(',', '')))
df['rating'] = df['rating'].apply(lambda x : float(x))

df.to_csv('cleaned_data.csv', index=False)