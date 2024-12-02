import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.simplefilter('ignore', FutureWarning)

# データを読み込む
df = pd.read_csv('./work/data/feature/fuutou.csv')
df = df.drop('得意先コード', axis=1)

# クラスタリング
sc = StandardScaler() #データの標準化
clustering_sc = sc.fit_transform(df)
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit(df)
df['cluster'] = clusters.labels_

# PCAでデータを2次元に削減する
x = clustering_sc
pca = PCA(n_components=2)
pca.fit(x)
x_pca = pca.transform(x)
pca_df = pd.DataFrame(x_pca)
pca_df['cluster'] = df['cluster'].values

# クラスタごとの平均値を計算
ctb_means = df.groupby('cluster').mean()

# クロス集計結果の表示
print("CTB平均値:")
print(ctb_means)
ctb_means.to_csv('./work/data/feature/fuutouctb.csv', index=False, encoding='utf-8')
print(ctb_means)

#プロット
fig = plt.figure(figsize = (9, 6))
for i in pca_df['cluster'].unique():
   tmp = pca_df.loc[pca_df['cluster']==i]
   plt.scatter(tmp[0],tmp[1])

# 各要素にDataFrameのインデックスの数字をラベルとして付ける
plt.legend()
plt.show()