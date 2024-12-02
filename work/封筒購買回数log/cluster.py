import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.simplefilter('ignore', FutureWarning)
from sklearn.decomposition import FactorAnalysis as FA


# データを読み込む
df = pd.read_excel('購買log因子得点.xlsx')

# クラスタリング
sc = StandardScaler() #データの標準化
clustering_sc = sc.fit_transform(df)
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(df)
df['cluster'] = clusters.labels_

# PCAでデータを2次元に削減する
x = clustering_sc
pca = PCA(n_components=2)
pca.fit(x)
x_pca = pca.transform(x)
pca_df = pd.DataFrame(x_pca)
pca_df['cluster'] = df['cluster'].values

# 第一主成分の固有ベクトル
eigenvector_1 = pca.components_[0]
print("第一主成分の固有ベクトル:", eigenvector_1)

# 第二主成分の固有ベクトル
eigenvector_2 = pca.components_[1]
print("第二主成分の固有ベクトル:", eigenvector_2)

# 寄与率と累積寄与率を表示する
print("寄与率:", pca.explained_variance_ratio_)
cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
print("累積寄与率:", cumulative_variance_ratio)


# # クラスタ中心を取得
# cluster_centers = pd.DataFrame(sc.inverse_transform(clusters.cluster_centers_), columns=df.columns[:-1])
# # クラスタ中心を表示
# print("クラスタ中心:")
# print(cluster_centers)


# クラスタごとの平均値を計算
ctb_means = df.groupby('cluster').mean()

# 購買平均
print("購買平均:")
print(ctb_means)
ctb_means.to_csv('./work/data/feature/cyubunnruictv.csv', index=False, encoding='utf-8')

# クラスタごとの人数を計算
cluster_sizes = df['cluster'].value_counts().sort_index()

# クラスタごとの人数の表示
print("各クラスタの顧客数:")
print(cluster_sizes)


# 各クラスタの構成比率を計算
total_samples = len(df)
cluster_compositions = cluster_sizes / total_samples * 100

# 構成比率を表示
print("各クラスタの構成比率:")
print(cluster_compositions)

# #プロット
# fig = plt.figure(figsize = (9, 6))
# for i in pca_df['cluster'].unique():
#    tmp = pca_df.loc[pca_df['cluster']==i]
#    # print(tmp)
#    plt.scatter(tmp[0],tmp[1])

# プロット
fig = plt.figure(figsize=(9, 6))

# Define the number of clusters
num_clusters = len(pca_df['cluster'].unique())

# Generate a list of random colors
colors = plt.cm.rainbow(np.linspace(0, 1, num_clusters))

for i, cluster in enumerate(pca_df['cluster'].unique()):
    tmp = pca_df.loc[pca_df['cluster'] == cluster]
    plt.scatter(tmp[0], tmp[1], label=f'Cluster {cluster}', color=colors[i], alpha=0.7)
# 各要素にDataFrameのインデックスの数字をラベルとして付ける
plt.legend()
plt.show()