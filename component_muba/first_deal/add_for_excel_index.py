####excel某列编号添加

import os
import pandas as pd

input_file = 'D:\zhongwgai.xlsx'
df = pd.read_excel(input_file)


if 'label' not in df.columns:
    df['label'] = ""
# 为'rename'列添加'ddsm'前缀和从1开始的数字编号
df['label'] = 'mias-' + (df.index + 1).astype(str)+'-label'

print(df)


output_file = 'D:\zhongwgai.xlsx'
df.to_excel(output_file, index=False)

print(f'Data with updated "rename" column saved to {output_file}')
