# 옵션 관련 데이터 import

import pandas as pd

df = pd.read_csv('product_options.csv', low_memory=False)

# product_code size_value color_value option_name
# print(df)

# 특정 컬럼의 종류
# print(df['color_value'].unique()[:100])

print(df[df['product_code'] == '2406478862'])


print(df[df['product_code'] == '2404929823'])

print(df[df['product_code'].isin(['2311997355','2311997410','2311997414','2405068674','2405069433','2405069435','2405097464','2405098113','2405098117'])])

print(df[df['product_code'].isin(['2301628144',    '2305800187' ,  '2307836141' ,   '2307836275' ,  '2307836337'])])



pd_csv = pd.read_csv('filtered_goods_no.csv' )
pd_list = pd_csv['goods_no'].tolist()


print(df[df['product_code'].isin(pd_list) == False]) # 없는 애들은 뺄까...

print(df[df['product_code'].isin(pd_list) == True])

print(df[df['product_code'] == '2210576591']) # 옵션 2개에 대해서는 2개의 option 값을 가지고 있음.




