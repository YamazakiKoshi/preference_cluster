import pandas as pd
import numpy as np

# Excelファイルの読み込み
df = pd.read_excel('./work/data/raw/購買データ_商品属性付き.xlsx')

# 得意先コードと商品名の列を抽出
subset_df = df[['受注日', '得意先コード', '商品名', '製品区分', 'サイズ・規格','チャネル']]
# '受注日'列が日付以外の値を含む行を除外
subset_df = subset_df[subset_df['受注日'].astype(str).str.match(r'\d{8}')]
# '受注日'列を日付型に変換
subset_df['受注日'] = pd.to_datetime(subset_df['受注日'], format='%Y%m%d')
# サイズ・規格の中に「封筒」という文字列が含まれるデータを抽出
filtered_df = subset_df[subset_df['サイズ・規格'].str.contains('封筒')]
# '受注日'が2019-01-07以降のデータに絞り込み
filtered_df = filtered_df[filtered_df['受注日'] >= '2019-01-07']

# 'チャネル'が通販サイトのデータに絞り込み
filtered_df = filtered_df[filtered_df['チャネル'].str.contains('通販サイト')]

# 新しいExcelファイルとして保存
file_path = '封筒.xlsx'
filtered_df.to_excel(file_path, index=False)


# 'サイズ・規格' 列のユニークな値とその出現回数を取得
size_counts = filtered_df['サイズ・規格'].value_counts().reset_index().rename(columns={'index': 'サイズ・規格', 'サイズ・規格': '回数'})
# # 新しいExcelファイルとして保存
# file_path = '属性.xlsx'
# size_counts.to_excel(file_path, index=False)


# 封筒.xlsxの読み込み
df = pd.read_excel('封筒.xlsx')
# 得意先ごとの購入回数を数える
purchase_counts = df['得意先コード'].value_counts()
# 購入回数が2回以上の得意先コードを取得
selected_customers = purchase_counts[purchase_counts >= 2].index
# 購入回数が2回以上の得意先のデータを抽出
filtered_df = df[df['得意先コード'].isin(selected_customers)]
# 新しいExcelファイルとして保存
filtered_df.to_csv('顧客.csv', index=False, encoding='utf-8')


# 顧客.csvの読み込み
df = pd.read_csv('顧客.csv', encoding='utf-8')
# 'サイズ・規格' 列のユニークな値を取得
size_types = df['サイズ・規格'].unique()
# 結果を表示
print(size_types)


#結果用データフレーム
result_df = pd.DataFrame()
result_df['得意先コード'] = df[['得意先コード']]


result_df['オーダーメイド_角２'] = (df['サイズ・規格'].str.contains('角２封筒')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角5'] = (df['サイズ・規格'].str.contains('角５封筒')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角7'] = (df['サイズ・規格'].str.contains('角７封筒')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角2封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('角２封筒\(アドヘア\)')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角5封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('角５封筒\(アドヘア\)')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角2封筒(テープ付)'] = (df['サイズ・規格'].str.contains('角２封筒\(テープ付\)')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_角7封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('角７封筒\（ホットメルト\）')&df['製品区分'].str.contains('オーダーメイド')).astype(int)


result_df['オーダーメイド_角2窓明封筒(テープつき)'] = (df['サイズ・規格'].str.contains('角２窓明封筒\（テープつき\）')&df['製品区分'].str.contains('オーダーメイド')).astype(int)


result_df['オーダーメイド_長3'] = (df['サイズ・規格'].str.contains('長３封筒')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['既製品_長4'] = (df['サイズ・規格'].str.contains('長４封筒')
                       &df['製品区分'].str.contains('既製品')
                       &~df['サイズ・規格'].str.contains('アドヘア')
                       &~df['サイズ・規格'].str.contains('テープつけ')
                       &~df['サイズ・規格'].str.contains('ホットメルト')).astype(int)


result_df['オーダーメイド_長3封筒(テープ付)'] = (df['サイズ・規格'].str.contains('長３封筒\(テープ付\)')&df['製品区分'].str.contains('オーダーメイド')).astype(int)


result_df['オーダーメイド_長3窓明封筒'] = (df['サイズ・規格'].str.contains('長３窓明')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('アドヘア')
                                &~df['サイズ・規格'].str.contains('テープつき')
                                &~df['サイズ・規格'].str.contains('ホットメルト')).astype(int)
result_df['オーダーメイド_長3窓明封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('長３窓明封筒\（アドヘア\）')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_長3窓明封筒(テープつき)'] = (df['サイズ・規格'].str.contains('長３窓明封筒\（テープつき\）')&df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_長3窓明封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('長３窓明封筒\（ホットメルト\）')&df['製品区分'].str.contains('オーダーメイド')).astype(int)


result_df['オーダーメイド_封筒'] = (df['サイズ・規格'].str.contains('封筒')
                           &df['製品区分'].str.contains('オーダーメイド')
                           &~df['サイズ・規格'].str.contains('角')
                           &~df['サイズ・規格'].str.contains('長')
                           &~df['サイズ・規格'].str.contains('洋')
                           &~df['サイズ・規格'].str.contains('叺')
                           &~df['サイズ・規格'].str.contains('窓明')
                           &~df['サイズ・規格'].str.contains('開封')
                           &~df['サイズ・規格'].str.contains('ガゼット')).astype(int)


result_df['オーダーメイド_封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('封筒\(アドヘア\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('窓明')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)
result_df['オーダーメイド_封筒(テープ付)'] = (df['サイズ・規格'].str.contains('封筒\(テープ付\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('窓明')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)
result_df['オーダーメイド_封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('封筒\(ホットメルト\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('窓明')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)


result_df['オーダーメイド_窓明封筒'] = (df['サイズ・規格'].str.contains('窓明封筒')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)
result_df['オーダーメイド_窓明封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('窓明封筒\(アドヘア\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)
result_df['オーダーメイド_窓明封筒(テープ付)'] = (df['サイズ・規格'].str.contains('窓明封筒\(テープ付\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('叺')
                                ).astype(int)
result_df['オーダーメイド_窓明封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('窓明封筒\(ホットメルト\)')
                                &df['製品区分'].str.contains('オーダーメイド')
                                &~df['サイズ・規格'].str.contains('角')
                                &~df['サイズ・規格'].str.contains('長')
                                &~df['サイズ・規格'].str.contains('叺')

                                ).astype(int)
result_df['開封封筒_オーダーメイド'] = (df['サイズ・規格'].str.contains('開封')&df['製品区分'].str.contains('オーダーメイド')).astype(int)


result_df['オーダーメイド_内叺貼封筒'] = (df['サイズ・規格'].str.contains('内叺貼封筒')
                           &df['製品区分'].str.contains('オーダーメイド')
                           &~df['サイズ・規格'].str.contains('窓明')
                           &~df['サイズ・規格'].str.contains('アドヘア')
                           &~df['サイズ・規格'].str.contains('テープ付')
                           &~df['サイズ・規格'].str.contains('ホットメルト')
                           &~df['サイズ・規格'].str.contains('アラビア')
                           &~df['サイズ・規格'].str.contains('大内')).astype(int)


result_df['オーダーメイド_内叺貼封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('内叺貼封筒\(アドヘア\)')
                                    &df['製品区分'].str.contains('オーダーメイド')
                                    &~df['サイズ・規格'].str.contains('窓明')
                                    &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('内叺貼封筒\(アドヘア\)')
                                    &df['製品区分'].str.contains('オーダーメイド')
                                    &~df['サイズ・規格'].str.contains('窓明')
                                    &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼封筒(テープ付)'] = (df['サイズ・規格'].str.contains('内叺貼封筒\(テープ付\)')
                                    &df['製品区分'].str.contains('オーダーメイド')
                                    &~df['サイズ・規格'].str.contains('窓明')
                                    &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('内叺貼封筒\(ホットメルト\)')
                                    &df['製品区分'].str.contains('オーダーメイド')
                                    &~df['サイズ・規格'].str.contains('窓明')
                                    &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼封筒(アラビア)'] = (df['サイズ・規格'].str.contains('内叺貼封筒\(アラビア\)')
                                    &df['製品区分'].str.contains('オーダーメイド')
                                    &~df['サイズ・規格'].str.contains('窓明')
                                    &~df['サイズ・規格'].str.contains('大内')).astype(int)


result_df['オーダーメイド_内叺貼窓明封筒'] = (df['サイズ・規格'].str.contains('内叺貼窓明')
                             &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼窓明封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('内叺貼窓明封筒\(アドヘア\)')
                                   &df['製品区分'].str.contains('オーダーメイド')
                                   &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼窓明封筒(テープ付)'] = (df['サイズ・規格'].str.contains('内叺貼窓明封筒\(テープ付\)')
                                   &df['製品区分'].str.contains('オーダーメイド')
                                   &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼窓明封筒(ホットメルト)'] = (df['サイズ・規格'].str.contains('内叺貼窓明封筒\(ホットメルト\)')
                                   &df['製品区分'].str.contains('オーダーメイド')
                                   &~df['サイズ・規格'].str.contains('大内')).astype(int)
result_df['オーダーメイド_内叺貼窓明封筒(アラビア)'] = (df['サイズ・規格'].str.contains('内叺貼窓明封筒\(アラビア\)')
                                   &df['製品区分'].str.contains('オーダーメイド')
                                   &~df['サイズ・規格'].str.contains('大内')).astype(int)

result_df['オーダーメイド_大内叺貼封筒'] = (df['サイズ・規格'].str.contains('大内叺貼')
                           &df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_大内叺貼封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('大内叺貼封筒\(アドヘア\)')
                                &~df['サイズ・規格'].str.contains('窓明')).astype(int)
result_df['オーダーメイド_大内叺貼窓明封筒'] = (df['サイズ・規格'].str.contains('大内叺貼窓明')
                                 &df['製品区分'].str.contains('オーダーメイド')).astype(int)
result_df['オーダーメイド_大内叺貼窓明封筒(アドヘア)'] = (df['サイズ・規格'].str.contains('大内叺貼窓明封筒\(アドヘア\)')
                                 &df['製品区分'].str.contains('オーダーメイド')).astype(int)

result_df['オーダーメイド_ガゼット貼封筒'] = (df['サイズ・規格'].str.contains('ガゼット')&df['製品区分'].str.contains('オーダーメイド')).astype(int)

result_df['既製品_アドヘア(角2)'] = (df['サイズ・規格'].str.contains('アドヘア\(角２封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_アドヘア(角3)'] = (df['サイズ・規格'].str.contains('アドヘア\(角３封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_アドヘア(角5)'] = (df['サイズ・規格'].str.contains('アドヘア\(角５封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_アドヘア(角6)'] = (df['サイズ・規格'].str.contains('アドヘア\(角６封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_アドヘア(長3)'] = (df['サイズ・規格'].str.contains('アドヘア\(長３封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_アドヘア(長4)'] = (df['サイズ・規格'].str.contains('アドヘア\(長４封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)

result_df['既製品_テープ付け(角0)'] = (df['サイズ・規格'].str.contains('テープ付け\(角０封筒\)')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープ付け(角1)'] = (df['サイズ・規格'].str.contains('テープ付け\（角１封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープ付け(角2)'] = (df['サイズ・規格'].str.contains('テープ付け\（角２封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープ付け(角3)'] = (df['サイズ・規格'].str.contains('テープ付け\（角３封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープ付け(角5)'] = (df['サイズ・規格'].str.contains('テープ付け\（角５封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(角6)'] = (df['サイズ・規格'].str.contains('テープつけ\（角６封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(角7)'] = (df['サイズ・規格'].str.contains('テープつけ\（角７封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(角8)'] = (df['サイズ・規格'].str.contains('テープつけ\（角８封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(長2)'] = (df['サイズ・規格'].str.contains('テープつけ\（長２封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(長3)'] = (df['サイズ・規格'].str.contains('テープつけ\（長３封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(長4)'] = (df['サイズ・規格'].str.contains('テープつけ\（長４封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_テープつけ(洋封筒)'] = (df['サイズ・規格'].str.contains('テープつけ\（洋封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)

result_df['既製品_ホットメルト(角2)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角２封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(角3)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角３封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(角5)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角５封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(角6)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角６封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(角7)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角７封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(角8)'] = (df['サイズ・規格'].str.contains('ホットメルト\（角８封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(長3)'] = (df['サイズ・規格'].str.contains('ホットメルト\（長３封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(長4)'] = (df['サイズ・規格'].str.contains('ホットメルト\（長４封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)
result_df['既製品_ホットメルト(洋封筒)'] = (df['サイズ・規格'].str.contains('ホットメルト\（洋封筒\）')&df['製品区分'].str.contains('既製品')).astype(int)

result_df['S貼'] = df['商品名'].str.contains('Ｓ貼').astype(int)
result_df['C貼'] = df['商品名'].str.contains('Ｃ貼').astype(int)
result_df['逆S'] = df['商品名'].str.contains('逆Ｓ貼').astype(int) #逆S貼



# IDごとに集計
result_df = result_df.groupby('得意先コード').sum().reset_index()

# 購買回数を log10(x + 1) で変換
purchase_columns = result_df.columns[1:]  # '得意先コード'以外の列を選択
result_df[purchase_columns] = np.log10(result_df[purchase_columns] + 1)

# 顧客ごとに統合
result_df.to_csv('./work/data/feature/size_log.csv', index=False, encoding='utf-8')
print(result_df)