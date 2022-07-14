# House Prices - Advanced Regression Techniques
## Predict sales prices and practice feature engineering, RFs, and gradient boosting

### 预测房屋价格
每个房屋有79个属性，在训练集中，给出了每个房屋对应的售价，你需要根据训练集中的数据，预测出测试集中每个房屋的售价是多少

### data目录中的文件介绍
- data_description.txt: 数据集中每列的详细描述
```txt
MSSubClass: Identifies the type of dwelling involved in the sale.	
        20	1-STORY 1946 & NEWER ALL STYLES
        30	1-STORY 1945 & OLDER
        40	1-STORY W/FINISHED ATTIC ALL AGES
        45	1-1/2 STORY - UNFINISHED ALL AGES
        50	1-1/2 STORY FINISHED ALL AGES
```
- train.csv: 训练数据，包括房屋ID，79个房屋属性，房屋售价
- test.csv: 测试数据，包括房屋ID， 79个房屋属性
最后参考sample_submission.csv得到你的预测结果文件，包括房屋id，房屋售价

# 参考
1. [分析数据](https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python)
2. [特征工程：分析数据特征是否缺失](https://www.kaggle.com/code/dgawlik/house-prices-eda)
3. [sklearn与线性回归](https://www.kaggle.com/code/juliencs/a-study-on-regression-applied-to-the-ames-dataset)
4. [正则化的线性回归模型](https://www.kaggle.com/code/apapiu/regularized-linear-models)
5. [完整解决方案例1-北京理工](https://bitdm.github.io/2020/projects/P08/final.html)
