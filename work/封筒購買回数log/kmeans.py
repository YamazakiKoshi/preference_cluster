import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.simplefilter('ignore', FutureWarning)
from sklearn.decomposition import FactorAnalysis as FA
import japanize_matplotlib



# データを読み込む
# df = pd.read_csv('./work/data/feature/koubailog.csv')
# df = df.drop('得意先コード', axis=1)
# # データを読み込む
df = pd.read_excel('購買log因子得点.xlsx')
# 標準化器を作成して標準得点を計算
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
df_standardized.to_csv("標準得点.csv",index=False)


# クラスタリング
sc = StandardScaler() #データの標準化
clustering_sc = sc.fit_transform(df)
kmeans = KMeans(n_clusters=7, random_state=0)
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
# # データフレームに変換
# df_factor_loadings = pd.DataFrame(eigenvector_1)
# # Excelファイルに保存
# excel_file_path = "固有ベクトル1.xlsx"
# df_factor_loadings.to_excel(excel_file_path, index=False)
# 第二主成分の固有ベクトル
eigenvector_2 = pca.components_[1]
print("第二主成分の固有ベクトル:", eigenvector_2)
# # データフレームに変換
# df_factor_loadings = pd.DataFrame(eigenvector_2)

# # Excelファイルに保存
# excel_file_path = "固有ベクトル2.xlsx"
# df_factor_loadings.to_excel(excel_file_path, index=False)

# 寄与率と累積寄与率を表示する
print("寄与率:", pca.explained_variance_ratio_)
cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
print("累積寄与率:", cumulative_variance_ratio)

# クラスタごとの平均値を計算
ctb_means = df.groupby('cluster').mean()

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
excel_file_path = "中心ベクトル.xlsx"
df_factor_loadings.to_excel(excel_file_path, index=False)

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


# # クラスタごとの中心ベクトルを可視化
# plt.figure(figsize=(12, 6))
# for i in range(len(df_cluster_centers)):
#     plt.plot(df_cluster_centers.columns, df_cluster_centers.iloc[i], label=f'Cluster {i}')
# plt.title('Cluster Centers')
# plt.xlabel('特徴量')
# plt.ylabel('Values')
# plt.legend()
# plt.show()


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
