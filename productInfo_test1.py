import pandas as pd

df = pd.read_csv('product_info.csv', low_memory=False)



# print(df.iloc[0][['goods_nm', 'goods_no']])
# print(df.iloc[53432:53441][['goods_nm', 'goods_no','opt_nm1', 'opt_nm2']])

# 컬럼의 값 종류
print(df['opt_nm1'].unique())

print(df[df['opt_nm1'] == '[본사정품]'][['goods_nm', 'goods_no', 'opt_nm1', 'opt_nm2']] )

df1 = df['opt_nm1']

df2 = {}

# 몇 개 존재하는 지 확인
for i in df1 :            
    if i not in df2.keys(): # key 값이 없다면
        df2[i] = 1
    else :
        df2[i] = df2[i] + 1
    #if pd.isna(i):
    #    print("i : " , i) # nan이라 갑이 들어가 있음

print("=========== df2[] ========== \n", df2)
# {'색상': 51697, nan: 468, '통합색상': 19, '컬러': 320, '선택': 9, 'SIZE': 16, 'COLOR': 129, '사이즈': 295, '옵션명1': 120, '바디케어 세트': 2, '핸드케어  
# 세트': 1, 'Colors': 1, 'SIZEF': 1, '호수(남성용)': 1, '스타일번호': 122, 'T0006324': 1, 'Color': 6, '옵션': 53,
'''
print(df[df['opt_nm1'] == '여행키트']['goods_no']) # 2406478862 => index[]

print(df[df['opt_nm1'] == '양말선택']['goods_no']) # 2404929823 => index[]

print(df[df['opt_nm1'] == '기본']['goods_no']) # 2311997355,2311997410,2311997414,2405068674,2405069433,2405069435,2405097464,2405098113,2405098117 => index[]

print(df[df['opt_nm1'] == 'COLOR']['goods_no'])  #2301628144    2305800187   2307836141    2307836275   2307836337


print(df[df['opt_nm1'] == 'nan']['goods_no'])  # 
'''

print(df[df['opt_nm1'] == '색상']['goods_no'])  # 2409164418  01P0000000025

df3 = df[df['opt_nm1'] == '색상']['goods_no']
df3.to_csv('filtered_goods_no.csv', index=False)

print(df[df['goods_nm'] == '블랑쉬 오 드 퍼퓸 100ml']['goods_no']) # 옵션 2개 가지는 향수에 대한 no : 2210576591
# print(df[df['goods_nm'] == '블랑쉬 오 드 퍼퓸 50ml'].to_json('check_json', orient='index'))

# goods_no 중복 체크
print(df[df['goods_no'].duplicated() == True]['goods_no']) # goods_no == NaN인 case 존재

print(df[df['normal_price'] == 0]['normal_price'])