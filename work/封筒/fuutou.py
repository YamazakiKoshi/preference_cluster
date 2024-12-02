import pandas as pd
import numpy as np


# '商品名' S貼りと逆S貼りの区別
def label_product(x):
    if isinstance(x, str) and '逆S貼' in x:
        return '逆S'
    else:
        return x

# Excelファイルの読み込み
df = pd.read_excel('./work/data/raw/購買データ_商品属性付き.xlsx')

# 得意先コードと商品名の列を抽出
subset_df = df[['得意先コード', '商品名','製品区分','サイズ・規格']]

# 封筒が付く商品名の条件でデータをフィルタリング
filtered_df = subset_df[subset_df['サイズ・規格'].str.contains('封筒')| subset_df['商品名'].str.contains('(封筒)')]
# 新しいExcelファイルとして保存
file_path = '封筒のみ.xlsx'
filtered_df.to_excel(file_path, index=False)

df1=pd.read_excel('封筒のみ.xlsx')


#結果用データフレーム
result_df = pd.DataFrame()
result_df['得意先コード'] = df1[['得意先コード']]


# 大分類
# result_df['封筒'] = df['サイズ・規格'].str.contains('封筒').astype(int)


result_df['かます'] = df1['商品名'].str.contains('かます').astype(int)
# result_df['洋封筒'] = (df['商品名'].str.contains('洋')).astype(int)
result_df['洋0'] = df1['商品名'].str.contains('洋０').astype(int)
result_df['洋2_オーダーメイド'] = (df1['商品名'].str.contains('洋２')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['洋2_既製品'] = (df1['商品名'].str.contains('洋２')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['洋長３_オーダーメイド'] = (df1['商品名'].str.contains('洋長３')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['洋長３_既製品'] = (df1['商品名'].str.contains('洋長３')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['洋４_オーダーメイド'] = (df1['商品名'].str.contains('洋４')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['洋４_既製品'] = (df1['商品名'].str.contains('洋４')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['洋５_オーダーメイド'] = (df1['商品名'].str.contains('洋５')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['洋５_既製品'] = (df1['商品名'].str.contains('洋５')&df1['製品区分'].str.contains('既製品')).astype(int)


# result_df['角封筒'] = (df['商品名'].str.contains('角') & ~df['商品名'].str.contains('角底')).astype(int)
result_df['角0_オーダーメイド'] = (df1['商品名'].str.contains('角０')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角0_既製品'] = (df1['商品名'].str.contains('角０')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角1_オーダーメイド'] = (df1['商品名'].str.contains('角１')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角1_既製品'] = (df1['商品名'].str.contains('角１')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角2_オーダーメイド'] = (df1['商品名'].str.contains('角２')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角2_既製品'] = (df1['商品名'].str.contains('角２')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角3_オーダーメイド'] = (df1['商品名'].str.contains('角３')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角3_既製品'] = (df1['商品名'].str.contains('角３')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角4_オーダーメイド'] = (df1['商品名'].str.contains('角４')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角4_既製品'] = (df1['商品名'].str.contains('角４')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角5_オーダーメイド'] = (df1['商品名'].str.contains('角５')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角5_既製品'] = (df1['商品名'].str.contains('角５')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角6_オーダーメイド'] = (df1['商品名'].str.contains('角６')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角6_既製品'] = (df1['商品名'].str.contains('角６')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角7_オーダーメイド'] = (df1['商品名'].str.contains('角７')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角7_既製品'] = (df1['商品名'].str.contains('角７')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角8_オーダーメイド'] = (df1['商品名'].str.contains('角８')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角8_既製品'] = (df1['商品名'].str.contains('角８')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角20_オーダーメイド'] = (df1['商品名'].str.contains('角２０')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角20_既製品'] = (df1['商品名'].str.contains('角２０')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角A3_オーダーメイド'] = (df1['商品名'].str.contains('角Ａ3')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角A3_既製品'] = (df1['商品名'].str.contains('角Ａ3')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['角A4_オーダーメイド'] = (df1['商品名'].str.contains('角Ａ４')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['角A4_既製品'] = (df1['商品名'].str.contains('角Ａ４')&df1['製品区分'].str.contains('既製品')).astype(int)

# result_df['長封筒'] = (df['商品名'].str.contains('長') & ~df['商品名'].str.contains('洋長')).astype(int)
result_df['長1_オーダーメイド'] = (df1['商品名'].str.contains('長１')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長1_既製品'] = (df1['商品名'].str.contains('長１')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['長2_オーダーメイド'] = (df1['商品名'].str.contains('長２')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長2_既製品'] = (df1['商品名'].str.contains('長２')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['長3_オーダーメイド'] = (df1['商品名'].str.contains('長３') & ~df1['商品名'].str.contains('洋長３')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長3_既製品'] = (df1['商品名'].str.contains('長３') & ~df1['商品名'].str.contains('洋長３')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['長4_オーダーメイド'] = (df1['商品名'].str.contains('長４')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長4_既製品'] = (df1['商品名'].str.contains('長４')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['長6_オーダーメイド'] = (df1['商品名'].str.contains('長６')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長6_既製品'] = (df1['商品名'].str.contains('長６')&df1['製品区分'].str.contains('既製品')).astype(int)
result_df['長40_オーダーメイド'] = (df1['商品名'].str.contains('長４０')&df1['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['長40_既製品'] = (df1['商品名'].str.contains('長４０')&df1['製品区分'].str.contains('既製品')).astype(int)

result_df['ガゼット'] = (df1['商品名'].str.contains('ガゼット') & ~df1['商品名'].str.contains('ガゼット袋')).astype(int)
result_df['チケット'] = (df1['商品名'].str.contains('チケット')&df1['サイズ・規格'].str.contains('封筒')).astype(int)

result_df['S貼'] = df1['商品名'].str.contains('Ｓ貼').astype(int)
result_df['C貼'] = df1['商品名'].str.contains('Ｃ貼').astype(int)
result_df['逆S'] = df1['商品名'].str.contains('逆Ｓ貼').astype(int) #逆S貼


# 顧客ごとに統合
result_df = result_df.groupby('得意先コード').max().reset_index()
result_df.to_csv('./work/data/feature/fuutouonly.csv', index=False, encoding='utf-8')
print(result_df)