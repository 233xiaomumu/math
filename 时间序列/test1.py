import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_excel(
    'math\时间序列\A1_17.xlsx',      # 文件路径
    header=0,              # 使用第一行作为列名（默认值）
    parse_dates=[0],       # 将第一列解析为日期时间类型
    index_col=0             # 可选：将第一列设为索引
)

# 查看数据
print(df)

result=seasonal_decompose(df)

result.plot()

plt.show()

time=pd.Series(df)

result_2=trend