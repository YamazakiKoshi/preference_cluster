# ライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# # データを読み込む
# df = pd.read_excel('購買log因子得点.xlsx')
# データを読み込む
df = pd.read_csv('./work/data/feature/koubailog.csv')
df = df.drop('得意先コード', axis=1)

# クラスタリングの実行
clu = linkage(df, method='ward', metric='euclidean')

# 描画領域の定義
plt.figure(num=None, figsize=(16, 9))

# 樹形図の作成・出力
dendrogram(clu)
plt.show()