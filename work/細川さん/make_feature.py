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
result_df['袋'] = df['サイズ・規格'].apply(lambda x: 1 if '袋' in x else 0)
result_df['はがき'] = df['サイズ・規格'].apply(lambda x: 1 if '印刷' in x else 0)

# # 中分類？小分類？
# result_df['角0'] = df['商品名'].apply(lambda x: 1 if '角０' in x else 0)
# result_df['角1'] = df['商品名'].apply(lambda x: 1 if '角１' in x else 0)
# result_df['角2'] = df['商品名'].apply(lambda x: 1 if '角２' in x else 0)
# result_df['角3'] = df['商品名'].apply(lambda x: 1 if '角３' in x else 0)
# result_df['角4'] = df['商品名'].apply(lambda x: 1 if '角４' in x else 0)
# result_df['角5'] = df['商品名'].apply(lambda x: 1 if '角５' in x else 0)
# result_df['角6'] = df['商品名'].apply(lambda x: 1 if '角６' in x else 0)
# result_df['角7'] = df['商品名'].apply(lambda x: 1 if '角７' in x else 0)
# result_df['角8'] = df['商品名'].apply(lambda x: 1 if '角８' in x else 0)

# result_df['長1'] = df['商品名'].apply(lambda x: 1 if '長１' in x else 0)
# result_df['長2'] = df['商品名'].apply(lambda x: 1 if '長２' in x else 0)
# result_df['長3'] = df['商品名'].apply(lambda x: 1 if '長３' in x else 0)
# result_df['長4'] = df['商品名'].apply(lambda x: 1 if '長４' in x else 0)

# # 貼り方？
# result_df['S貼'] = df['商品名'].apply(lambda x: 1 if 'Ｓ貼' in x else 0)
# result_df['C貼'] = df['商品名'].apply(lambda x: 1 if 'Ｃ貼' in x else 0)
# result_df['逆S'] = df['商品名'].apply(lambda x: 1 if '逆Ｓ貼' in x else 0) #逆S貼
# result_df['かます'] = df['商品名'].apply(lambda x: 1 if 'かます' in x else 0)

#オーダメイド or 既製品？

# 顧客ごとに統合
result_df = result_df.groupby('得意先コード').max().reset_index()
result_df.to_csv('./work/data/feature/feature.csv', index=False, encoding='utf-8')
print(result_df)