import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# データを読み込む
df = pd.read_csv('./work/data/feature/fuutouonly.csv')
df = df.drop('得意先コード', axis=1)

# 標準化器を作成して標準得点を計算
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# PCAで2次元に削減
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df_standardized), columns=['PC1', 'PC2'])

# K-meansのモデル構築
kmeans = KMeans(n_clusters=6, random_state=0)  # クラスタの数は適宜変更してください
clusters = kmeans.fit_predict(df_standardized)
df_pca['cluster'] = clusters

# 結果をCSVファイルに出力
df_pca.to_csv('PCAクラスタリング結果.csv', index=False)

# プロット
plt.figure(figsize=(10, 6))
for cluster in df_pca['cluster'].unique():
    plt.scatter(df_pca[df_pca['cluster'] == cluster]['PC1'], df_pca[df_pca['cluster'] == cluster]['PC2'], label=f'Cluster {cluster}')

plt.title('PCA K-means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()


