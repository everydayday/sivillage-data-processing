import requests, json
import pandas as pd
import time

URL = 'http://localhost:8080/v1/products'

headers = {'Content-Type': 'application/json'}   # data 주고 받는 형식 지정

# data 불러오기
df = pd.read_csv('merged_product.csv')

print(df.count())

# 데이터 db에 입력하기
# 8184 개 정도 들어감
# 나머지는 500번 오류 발생 => imageUrl에 goodsno 붙여주면 되어 있음
for idx, row in df.iterrows():  
  data ={
  "productCode": row['goods_no'],
  "productName": row['goods_nm'],
  "detail": 'https://m-goods.sivillage.com/goods/getGoodDescCont.siv?goods_no=' + str(row['goods_no']),
  "standardPrice": row['normal_price'],
  "discountPrice": row['cust_sale_price']
}
  response = requests.post(URL, data = json.dumps(data), headers= headers)
  time.sleep(0.000005)  # 단시간 너무 많은 서버와의 연결 -> delay 주기 : 50000개 넣으려니 너무 시간 많이 걸림
  print(response.status_code)
  









# response = requests.get(URL, params= data1)
# response = requests.get(URL) # connection OK

