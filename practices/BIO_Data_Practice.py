
import pandas as pd
df=pd.read_excel("./商品属性表1 0707.xlsx",sheet_name="碧欧泉小程序")
df

data1_product_name=df.loc[0:96,'产品名称']
data1_product_name

product_names1=list(data1_product_name)
product_names1

df=pd.read_excel("./BIO7月活动话术-6.30改 商品匹配.xlsx",sheet_name="6.30-7.12")
df

for idx, _ in df.iterrows():
    if not isinstance(df.iloc[idx,5], str):
        continue
    df.iloc[idx,5] = df.iloc[idx,5].replace("\n","<label class=格式,value=回车><\label>")
df.to_excel("./enter_label.xlsx", index=False)

df.columns

data2_product_name=df.loc[0:84,'Unnamed: 3']
data2_product_name

product_names2=list(data2_product_name)
product_names2

for product_name in product_names2:
    if product_name not in product_names1:
        print(product_name)

data3_product_name=df.loc[0:84,'Unnamed: 5']
data3_product_name

product_names3=list(data3_product_name)
product_names3

data3_product_name.replace('\n',"<label class=格式,value=回车><\label>").values

for product_name in product_names3:
    enter_label=product_name.replace('\n','<label class=格式,value=回车><\label>')
    print(enter_label)
