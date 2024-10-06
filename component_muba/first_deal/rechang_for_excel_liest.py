import os
import pandas as pd

input_file = 'D:\zhongwgai.xlsx'
df = pd.read_excel(input_file)
#weiba_dir = '.txt'


if 'rename' not in df.columns:
    df['rename'] = ""
#上面代码为构建的根据列！！
# 为某列构造新的字符
for index, row in df.iterrows():
    mid_patha = row['ID']
    df.at[index, 'everypath'] = f'folder_{mid_patha}\{mid_patha}'

# 查看结果
print(df)


output_file = 'D:\pythonwork\pythonProject\miaschange\\note\\notemias.xlsx'
df.to_excel(output_file, index=False)

print(f'Data with updated "txt" column saved to {output_file}')
