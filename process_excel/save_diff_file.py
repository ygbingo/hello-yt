"""
把单元格按不同行存到不同的文件中
"""
from typing import Any
import pandas as pd
from pandas import DataFrame

def read_data(file_path) -> DataFrame:
    # TODO: 处理获取数据的方法，并返回DataFrame数据

    df = DataFrame(data={"文件名称":["file1", "file2"], "value1": ["x1", "x2"], "value2": ["y1", "y2"]})

    return df

def save_file(data: Any, file_path: str):
    # TODO: 判断一下file_path是否包含"/", 想办法解决该问题，提示os.makedirs(path), os.path.exists(path)

    # 假设data是一个list
    with open(file_path, "w") as f:
        f.writelines(data)
    pass

def main():
    df = read_data()
    for idx, row in df.iterrows():
        """
        - idx: 行的索引, 这里其实没用到这个索引，可以用_代替
        - row: 每行的值，假设dataframe每行是: 文件名称, value1, value2, 那么每个row就能对应三个值，如下
        """
        file_name, value1, value2 = row
        data = [value1, value2]
        save_file(data, file_name)

main()    

