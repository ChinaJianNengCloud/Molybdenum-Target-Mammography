###某列继续添加内容时使用
import pandas as pd


input_file = 'D:\pythonwork\pythonProject\\totaldata\Integrated.xlsx'
df = pd.read_excel(input_file)

column_name = 'retxt'

if column_name in df.columns:
    # 为该列的每个单元格添加 '.jpg' 后缀
    df[column_name] = df[column_name].astype(str) + '.jpg'
    print(df)

    output_file = 'D:\pythonwork\pythonProject\\totaldata\Integrated.xlsx'
    df.to_excel(output_file, index=False)

    print(f'Data with updated "{column_name}" column saved to {output_file}')
else:
    print(f'"{column_name}" column not found in the Excel file.')
