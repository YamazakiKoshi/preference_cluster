import pandas as pd

# '商品名' S貼りと逆S貼りの区別
def label_product(x):
    if isinstance(x, str) and '逆S貼' in x:
        return '逆S'
    else:
        return x

df = pd.read_excel('./work/data/raw/購買データ_商品属性付き.xlsx')
df['商品名'] = df['商品名'].apply(label_product)

# 格納用
result_df = pd.DataFrame()
result_df = df[['得意先コード']]

# 大分類
result_df['封筒'] = df['サイズ・規格'].apply(lambda x: 1 if '封筒' in x else 0)

# 角 or 長？

# 中分類？小分類？
result_df['洋封筒'] = df['商品名'].apply(lambda x: 1 if '洋' in x else 0)
result_df['和封筒(長)'] = df['サイズ・規格'].apply(lambda x: 1 if '長' in x else 0)
result_df['和封筒(角)'] = df['サイズ・規格'].apply(lambda x: 1 if '角' in x else 0)

#オーダメイド or 既製品？

# 顧客ごとに統合
result_df = result_df.groupby('得意先コード').max().reset_index()
result_df.to_csv('./work/data/feature/fuutou.csv', index=False, encoding='utf-8')
print(result_df)