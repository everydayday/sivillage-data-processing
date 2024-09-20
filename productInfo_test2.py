import pandas as pd

df = pd.read_csv('product_info.csv', low_memory=False)



# 컬럼의 값 종류
print(df['opt_nm2'].unique())

#print(df[df['opt_nm1'] == '[본사정품]'][['goods_nm', 'goods_no', 'opt_nm1', 'opt_nm2']] )

df1 = df['opt_nm1']

df2 = {}

# 몇 개 존재하는 지 확인
for i in df1 :            
    if i not in df2.keys(): # key 값이 없다면
        df2[i] = 1
    else :
        df2[i] = df2[i] + 1
    if pd.isna(i):
       print("i : " , i) # nan이라 갑이 들어가 있음

print("=========== df2[] ========== \n", df2)
