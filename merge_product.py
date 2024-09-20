import pandas as pd

'''
# === product =====
1. productCode : goods_no
2. name : goods_nm
3. isOneSale
4. detail :  <1> detail
5. standardPrice : normal_price
6. discountPrice : cust_sale_price

'''



df1 = pd.read_csv('product_detail.csv') # detail 정보
df1.columns = ['goods_no', 'detail']
# print(df1) # 53441

# goods_no goods_nm, opt_nm1, opt_nm2, cust_sale_price, normal_price, brand_no, goods_save_amt, 
df2 = pd.read_csv('product_info.csv')   
# print(df2) # 53441

df21 = df2[['goods_no', 'goods_nm', 'normal_price', 'cust_sale_price']]
# print(df21)
df3 = pd.merge(df1, df21, how='inner', on='goods_no' ) 

# print(df3)  # 8184 rows => 겹치는 goods_no이 8184개다.

'''
 - product_info 기준으로 데이터 입력하기
 - 일단 겹치는 8184개만 해보기
'''

# 데이터 전처리
# print(df21[df21['normal_price'].isna()]['normal_price'])
df21.loc[df21['normal_price'].isna(), 'normal_price'] = 0  # NaN : 0 으로 처리하기
# print(df21[df21['normal_price'] == 0]['normal_price'])

# print(df21.loc[df21['cust_sale_price'].isna(), 'cust_sale_price'])
df21.loc[df21['cust_sale_price'].isna(), 'cust_sale_price'] = 0


df4 = pd.merge(df21, df1, how='left')   
# print(df4[df4['detail'].isna()])  # 45257 개 겹치지 않음
# print(df4)

df4.to_csv('merged_product.csv')






