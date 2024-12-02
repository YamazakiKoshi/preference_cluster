import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 標準化されたデータを読み込む
df_standardized = pd.read_csv('内訳標準得点.csv')

# K-meansのモデル構築
kmeans = KMeans(n_clusters=15,random_state=0)  # クラスタの数は適宜変更してください
clusters = kmeans.fit_predict(df_standardized)
df_standardized['cluster'] = clusters
# 結果をCSVファイルに出力
df_standardized.to_csv('クラスタリング結果.csv', index=False)

# PCAでデータを2次元に削減する
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df_standardized), columns=['PC1', 'PC2'])
df_pca['cluster'] = df_standardized['cluster']


# クラスタごとの中心ベクトルを取得
cluster_centers = kmeans.cluster_centers_
print(cluster_centers)

# データフレームに変換して表示
df_cluster_centers = pd.DataFrame(cluster_centers, columns=df_standardized.columns[:-1])
print("各クラスタの中心ベクトル:")
print(df_cluster_centers)
# データフレームに変換
df_factor_loadings = pd.DataFrame(df_cluster_centers)
# Excelファイルに保存
excel_file_path = "標準得点中心ベクトル.xlsx"
df_factor_loadings.to_excel(excel_file_path, index=False)
# クラスタごとの人数を計算
cluster_sizes = df_standardized['cluster'].value_counts().sort_index()

# クラスタごとの人数の表示
print("各クラスタの顧客数:")
print(cluster_sizes)

# 各クラスタの構成比率を計算
total_samples = len(df_standardized)
cluster_compositions = cluster_sizes / total_samples * 100

# 構成比率を表示
print("各クラスタの構成比率:")
print(cluster_compositions)

# クラスタ数の範囲を指定
max_clusters = 20
inertia = []

# エルボー法を用いて最適なクラスタ数を見つける
for n_clusters in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(df_standardized)
    inertia.append(kmeans.inertia_)

# エルボー法のプロット
plt.plot(range(1, max_clusters + 1), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-cluster Sum of Squares (Inertia)')
plt.title('Elbow Method for Optimal Cluster Number')
plt.show()

# プロット
plt.figure(figsize=(10, 6))
for cluster in df_pca['cluster'].unique():
    tmp = df_pca[df_pca['cluster'] == cluster]
    plt.scatter(tmp['PC1'], tmp['PC2'], label=f'Cluster {cluster}')

plt.title('K-means Clustering with PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()