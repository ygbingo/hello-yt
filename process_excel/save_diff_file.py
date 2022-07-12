"""
把单元格按不同行存到不同的文件中
"""
import os
from typing import Any
import pandas as pd
from pandas import DataFrame

def read_data(file_path) -> DataFrame:
    # TODO: 处理获取数据的方法，并返回DataFrame数据
    data1=pd.read_excel("./党史图谱-总表-0412.xlsx",sheet_name="事件表")
    data2=data1.loc[0:138,['事件名称','小标题']]
    data3=pd.DataFrame((x.split('\n')for x in data2['小标题']),columns=['1','2','3','4'])
    data4=data3.loc[:,['1','2','3']]
    data5=pd.merge(data2.loc[0:138,'事件名称'],data4,left_index=True, right_index=True)
    data6=data5.replace({"航天梦/航天强国":"航天梦",'大生产运动\u3000':"大生产运动",'重庆谈判\u3000':"重庆谈判","延安整风运动\u3000":"延安整风运动","土地制度改革\u3000":"土地改革制度","中华人民共和国成立70年/建国70年":"中华人民共和国成立70周年"})
    df = data6
#     df = DataFrame(data={"文件名称":["file1", "file2"], "value1": ["x1", "x2"], "value2": ["y1", "y2"]})

    return df

def save_file(data: Any, file_path: str):
    # TODO: 判断一下file_path是否包含"/", 想办法解决该问题，提示os.makedirs(path), os.path.exists(path)
    # 假设data是一个list
   
    with open(file_path+".txt", "w") as f:
         f.writelines(data)
    pass
def main():
    df = read_data("./党史图谱-总表-0412.xlsx")
    for idx, row in df.iterrows():
        """
        - idx: 行的索引, 这里其实没用到这个索引，可以用_代替
        - row: 每行的值，假设dataframe每行是: 文件名称, value1, value2, 那么每个row就能对应三个值，如下
        """
        file_name, value1, value2, value3 = row
        if pd.isna(file_name): 
            continue
        data = [str(value1), str(value2), str(value3)]
        save_file(data, file_name)

main()    
