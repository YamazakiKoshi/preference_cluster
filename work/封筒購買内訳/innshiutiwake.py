# ライブラリのインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from factor_analyzer import FactorAnalyzer

# データの読み込み
df = pd.read_csv("./work/data/feature/utiwake.csv", encoding="utf-8")
df = df.drop('得意先コード', axis=1)
# 標準化されたデータを読み込む
# df = pd.read_csv('標準得点.csv')

# データの正規化
df_workers_normalized = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)

# 変数の標準化
df_workers_std = df.apply(lambda x: (x - x.mean()) / x.std(), axis=0)


# NaN を含む行がないか確認　今回エラーが出てるのは相関の値？
# print("NaN の有無:", df_workers_std.corr().isna().any().any())
# print("NaN の有無:", df.isna().any().any())


# print("inf の有無:", np.isinf(df_workers_std.corr()).any().any())
# print("inf の有無:", np.isinf(df_workers).any().any())



# NaNを含むままで固有値を求める
ei = np.linalg.eigvals(df_workers_std.corr())
print(ei)
# データフレームに変換
df_factor_loadings = pd.DataFrame(ei)

# Excelファイルに保存
excel_file_path = "内訳固有値.xlsx"
df_factor_loadings.to_excel(excel_file_path, index=False)

# 因子分析の実行
fa = FactorAnalyzer(n_factors=16,rotation="oblimin",method="ml")
fa.fit(df_workers_std)

# 因子負荷量，共通性
loadings_df = pd.DataFrame(fa.loadings_, columns=["第１因子", "第２因子","第3因子","第4因子","第5因子"
                                                  ,"第6因子", "第7因子","第8因子","第9因子","第10因子"
                                                  ,"第11因子", "第12因子","第13因子","第14因子","第15因子"
                                                  ,"第16因子"])
loadings_df.index = df.columns
loadings_df["共通性"] = fa.get_communalities()
loadings_df["独自性"] = fa.get_uniquenesses()
print(loadings_df)

# データフレームに変換
df_factor_loadings = pd.DataFrame(loadings_df)

# Excelファイルに保存
excel_file_path = "内訳因子負荷量.xlsx"

df_factor_loadings.to_excel(excel_file_path, index=False)


# # 因子負荷量行列を使用して因子間相関を計算
# factor_loadings = fa.loadings_
# factor_correlation = np.corrcoef(factor_loadings, rowvar=False)
# print(factor_correlation)
# # 因子間相関のためのDataFrameを作成
# factor_correlation_df = pd.DataFrame(factor_correlation, 
#                                      columns=["第１因子", "第２因子","第3因子","第4因子","第5因子"
#                                                   ,"第6因子", "第7因子","第8因子","第9因子","第10因子"
#                                                   ,"第11因子", "第12因子","第13因子","第14因子","第15因子"
#                                                   ,"第16因子","第17因子","第18因子","第19因子", "第20因子","第21因子","第22因子","第23因子"], 
#                                      index=["第１因子", "第２因子","第3因子","第4因子","第5因子"
#                                                   ,"第6因子", "第7因子","第8因子","第9因子","第10因子"
#                                                   ,"第11因子", "第12因子","第13因子","第14因子","第15因子"
#                                                   ,"第16因子","第17因子","第18因子","第19因子", "第20因子","第21因子","第22因子","第23因子"])

# # 結果をExcelファイルに保存
# excel_file_path_correlation = "内訳因子間相関.xlsx"
# factor_correlation_df.to_excel(excel_file_path_correlation, index=False)


# # 因子負荷量の二乗和，寄与率，累積寄与率
# var = fa.get_factor_variance()
# df_var = pd.DataFrame(list(zip(var[0], var[1], var[2])), 
#                       index=["第１因子", "第２因子","第3因子","第4因子","第5因子"
#                                                   ,"第6因子", "第7因子","第8因子","第9因子","第10因子"
#                                                   ,"第11因子", "第12因子","第13因子","第14因子","第15因子"
#                                                   ,"第16因子","第17因子","第18因子","第19因子", "第20因子","第21因子","第22因子","第23因子"], 
#                       columns=["因子負荷量の二乗和", "寄与率", "累積寄与率"])
# print(df_var.T)
# # データフレームに変換
# df_factor_loadings = pd.DataFrame(df_var.T)

# # Excelファイルに保存
# excel_file_path = "内訳寄与率.xlsx"
# df_factor_loadings.to_excel(excel_file_path, index=False)


# 因子得点の計算
factor_scores = fa.transform(df_workers_std)
# NumPy array を DataFrame に変換
df_factor_scores = pd.DataFrame(factor_scores, columns=[f"因子{i+1}" for i in range(fa.n_factors)])
# データフレームに因子得点を追加
df_with_factor_scores = pd.concat([df_workers_std, df_factor_scores], axis=1)
# 因子得点だけを含むデータフレーム
df_factor_only = df_with_factor_scores.iloc[:, -fa.n_factors:]
# データフレームをExcelファイルに保存
df_factor_only.to_excel("購買内訳因子得点.xlsx", index=False)
print(df_factor_only)

# バイプロットの作図
score = fa.transform(df_workers_std)
coeff = fa.loadings_.T
fa1 = 0
fa2 = 1
labels = df.columns
annotations = df.index
xs = score[:, fa1]
ys = score[:, fa2]
n = score.shape[1]
scalex = 1.0 / (xs.max() - xs.min())
scaley = 1.0 / (ys.max() - ys.min())
X = xs * scalex
Y = ys * scaley
for i, label in enumerate(annotations):
    plt.annotate(label, (X[i], Y[i]))
for j in range(coeff.shape[1]):
    plt.arrow(0, 0, coeff[fa1, j], coeff[fa2, j], color='r', alpha=0.5, 
              head_width=0.03, head_length=0.015)
    plt.text(coeff[fa1, j] * 1.15, coeff[fa2, j] * 1.15, labels[j], color='r', 
             ha='center', va='center')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("第１因子")
plt.ylabel("第２因子")
plt.grid()
plt.show()