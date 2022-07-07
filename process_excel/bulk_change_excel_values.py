"""
批量修改excel的值
"""
import pandas as pd

REMOVE_STR = "\n"
REPLACE_STR = "<label>回车<\label>"

file_path = "../data/BIO7月活动话术-6.30改 商品匹配 2.xlsx"
result_file_path = "../data/result.xlsx"

SHEET_NAME = "6.30-7.12"
COL_NAME = 5

excel = pd.ExcelFile(file_path)
df = excel.parse(sheet_name=SHEET_NAME)

for idx, _ in df.iterrows():
    if not isinstance(df.iloc[idx, COL_NAME], str):
        continue
    df.iloc[idx, COL_NAME] = df.iloc[idx, COL_NAME].replace(REMOVE_STR, REPLACE_STR)

df.to_excel(result_file_path, sheet_name=SHEET_NAME, index=False)
