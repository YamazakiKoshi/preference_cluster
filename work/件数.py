import pandas as pd

# Excelファイルからデータを読み込む
df = pd.read_excel('./work/data/raw/購買データ_商品属性付き.xlsx')

# 商品名のラベルから「封筒」「袋」「はがき」の各件数を取得
count_envelope = df[df['サイズ・規格'].str.contains('封筒')]['商品名'].count()
count_bag = df[df['サイズ・規格'].str.contains('袋')]['商品名'].count()
count_postcard = df[df['サイズ・規格'].str.contains('印刷')]['商品名'].count()

# 結果を出力
print("封筒の件数:", count_envelope)
print("袋の件数:", count_bag)
print("はがきの件数:", count_postcard)

# 合計件数
total_count = count_envelope + count_bag + count_postcard

# 構成比率の計算
ratio_envelope = count_envelope / total_count * 100
ratio_bag = count_bag / total_count * 100
ratio_postcard = count_postcard / total_count * 100

# 結果を出力
print("封筒の構成比率:", ratio_envelope, "%")
print("袋の構成比率:", ratio_bag, "%")
print("はがきの構成比率:", ratio_postcard, "%")
