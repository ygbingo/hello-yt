import pandas as pd

ORI_FILE_PATH = "../data/BIO7月活动话术-6.30改 商品匹配 2.xlsx"
ORI_SHEET_NAME = "6.30-7.12"
ORI_COL_NUM = 3

COM_FILE_PATH = "../data/商品属性表1 0707.xlsx"
COM_SHEET_NAME = "碧欧泉官网"
COM_COL_NUM = 0

ori_df = pd.read_excel(ORI_FILE_PATH, sheet_name=ORI_SHEET_NAME)
com_df = pd.read_excel(COM_FILE_PATH, sheet_name=COM_SHEET_NAME)

ori_product_names = set(list(ori_df.iloc[:, ORI_COL_NUM]))
com_product_names = set(list(com_df.iloc[:, COM_COL_NUM]))

print(ori_product_names - com_product_names)

with open("../data/different_res.txt", "w") as writer:
    writer.writelines(list(ori_product_names - com_product_names))
