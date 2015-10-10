import pandas as pd
df = pd.read_csv('unicodeProduct.csv', encoding = 'utf-8')

small_df = df[['Brand', 'Title', 'Colors']]

small_df.to_csv('ToSearchOnAmazon.csv', index = False)