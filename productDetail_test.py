import pandas as pd

df = pd.read_csv('product_detail.csv')

df.columns = ['goods_nm', 'detail']

df2 = df[df['goods_nm'].isna()]

print(df) # na 없네