import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# # データを読み込む
# df = pd.read_excel('./封筒/封筒因子得点.xlsx')
# データを読み込む
df = pd.read_csv('./work/data/feature/fuutouonly.csv')
df = df.drop('得意先コード', axis=1)

# データの標準化
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
# K-means++のモデル構築
kmeans = KMeans(n_clusters=7, init='k-means++', random_state=0)
# モデル実行（クラスタリング）
clusters = kmeans.fit_predict(df_scaled)
df['cluster'] = clusters

#結果をcsvファイルに出力
df.to_csv("kmeans++.csv", index=False )

# PCAでデータを2次元に削減する
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df_scaled), columns=['PC1', 'PC2'])
df_pca['cluster'] = df['cluster']

# # 第一主成分の固有ベクトル
# eigenvector_1 = pca.components_[0]
# print("第一主成分の固有ベクトル:", eigenvector_1)
# #洋4_既製品

# # 第二主成分の固有ベクトル
# eigenvector_2 = pca.components_[1]
# print("第二主成分の固有ベクトル:", eigenvector_2)
#洋5_既製品

# クラスタごとの人数を計算
cluster_sizes = df['cluster'].value_counts().sort_index()

# 各クラスタの構成比率を計算
total_samples = len(df)
cluster_compositions = cluster_sizes / total_samples * 100

# 結果の表示
print("\n各クラスタの顧客数:")
print(cluster_sizes)
print("\n各クラスタの構成比率:")
print(cluster_compositions)

# # 各クラスタの平均値を計算
# cluster_means = df.groupby('cluster').mean()

# # 各クラスタの中央値を計算
# cluster_medians = df.groupby('cluster').median()

# # 各クラスタの標準偏差を計算
# cluster_std_devs = df.groupby('cluster').std()

# # 表示
# print("各クラスタの平均値:")
# print(cluster_means)

# print("\n各クラスタの中央値:")
# print(cluster_medians)

# print("\n各クラスタの標準偏差:")
# print(cluster_std_devs)
# クラスタごとの中心ベクトルを取得
cluster_centers = kmeans.cluster_centers_
print(cluster_centers)
# データフレームに変換して表示
df_cluster_centers = pd.DataFrame(cluster_centers, columns=df.columns[:-1])
print("各クラスタの中心ベクトル:")
print(df_cluster_centers)
# データフレームに変換
df_factor_loadings = pd.DataFrame(df_cluster_centers)
# Excelファイルに保存
excel_file_path = "中心ベクトル2.xlsx"
df_factor_loadings.to_excel(excel_file_path, index=False)
# プロット
plt.figure(figsize=(10, 6))
for cluster in df['cluster'].unique():
    plt.scatter(df_pca[df_pca['cluster'] == cluster]['PC1'], df_pca[df_pca['cluster'] == cluster]['PC2'], label=f'Cluster {cluster}')

plt.title('K-means++ Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()