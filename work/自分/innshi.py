# ライブラリのインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from factor_analyzer import FactorAnalyzer

# # データの読み込み
# df_workers = pd.read_csv("./work/自分/自分.csv", encoding="utf-8")
# df_workers = df_workers.drop('得意先コード', axis=1)
# # # データの読み込み
df_workers = pd.read_csv("./work/自分/自分.csv", encoding="utf-8")
df_workers = df_workers.drop('得意先コード', axis=1)

# 変数の標準化
df_workers_std = df_workers.apply(lambda x: (x - x.mean()) / x.std(), axis=0)
# # NaN を含む行がないか確認　今回エラーが出てるのは相関の値？
# print("NaN の有無:", df_workers_std.corr().isna().any().any())
# print("NaN の有無:", df_workers.isna().any().any())


# NaNを含むままで固有値を求める
ei = np.linalg.eigvals(df_workers_std.corr())
print(ei)
# データフレームに変換
df_factor_loadings = pd.DataFrame(ei)

# Excelファイルに保存
excel_file_path = "自分固有値.xlsx"
df_factor_loadings.to_excel(excel_file_path, index=False)

# 因子分析の実行（最尤法を使用）
fa_ml = FactorAnalyzer(n_factors=21, method='uls', rotation="oblimin")
fa_ml.fit(df_workers_std)



# 因子負荷量，共通性
loadings_df_ml = pd.DataFrame(fa_ml.loadings_, columns=["第1因子", "第2因子", "第3因子", "第4因子", "第5因子",
                                                        "第6因子", "第7因子", "第8因子", "第9因子", "第10因子",
                                                        "第11因子", "第12因子", "第13因子","第14因子", "第15因子", "第16因子", "第17因子", "第18因子",
                                                        "第19因子", "第20因子", "第21因子"])
loadings_df_ml.index = df_workers.columns
loadings_df_ml["共通性"] = fa_ml.get_communalities()
loadings_df_ml["独自性"] = fa_ml.get_uniquenesses()
print(loadings_df_ml)

# データフレームに変換
df_factor_loadings_ml = pd.DataFrame(loadings_df_ml)

# Excelファイルに保存
excel_file_path_ml = "自分因子負荷量.xlsx"
df_factor_loadings_ml.to_excel(excel_file_path_ml, index=False)



# 因子負荷量の二乗和，寄与率，累積寄与率
var_ml = fa_ml.get_factor_variance()
df_var_ml = pd.DataFrame(list(zip(var_ml[0], var_ml[1], var_ml[2])), 
                      index=["第1因子", "第2因子", "第3因子", "第4因子", "第5因子",
                                                        "第6因子", "第7因子", "第8因子", "第9因子", "第10因子",
                                                        "第11因子", "第12因子", "第13因子","第14因子", "第15因子", "第16因子", "第17因子", "第18因子",
                                                        "第19因子", "第20因子", "第21因子"], 
                      columns=["因子負荷量の二乗和", "寄与率", "累積寄与率"])
print(df_var_ml.T)
# データフレームに変換
df_factor_loadings_ml = pd.DataFrame(df_var_ml.T)

# Excelファイルに保存
excel_file_path_ml = "自分寄与率.xlsx"
df_factor_loadings_ml.to_excel(excel_file_path_ml, index=False)


# 因子負荷量行列を使用して因子間相関を計算
factor_loadings = fa_ml.loadings_
factor_correlation = np.corrcoef(factor_loadings, rowvar=False)
print(factor_correlation)
# 因子間相関のためのDataFrameを作成
factor_correlation_df = pd.DataFrame(factor_correlation, 
                                     columns=["第1因子", "第2因子", "第3因子", "第4因子", "第5因子",
                                                        "第6因子", "第7因子", "第8因子", "第9因子", "第10因子",
                                                        "第11因子", "第12因子", "第13因子","第14因子", "第15因子", "第16因子", "第17因子", "第18因子",
                                                        "第19因子", "第20因子", "第21因子"],
                                     index=["第1因子", "第2因子", "第3因子", "第4因子", "第5因子",
                                                        "第6因子", "第7因子", "第8因子", "第9因子", "第10因子",
                                                        "第11因子", "第12因子", "第13因子","第14因子", "第15因子", "第16因子", "第17因子", "第18因子",
                                                        "第19因子", "第20因子", "第21因子"])
# 結果をExcelファイルに保存
excel_file_path_correlation = "自分因子間相関.xlsx"
factor_correlation_df.to_excel(excel_file_path_correlation, index=False)

# 因子得点の計算
factor_scores = fa_ml.transform(df_workers_std)
# NumPy array を DataFrame に変換
df_factor_scores = pd.DataFrame(factor_scores, columns=[f"因子{i+1}" for i in range(fa_ml.n_factors)])
# データフレームに因子得点を追加
df_with_factor_scores = pd.concat([df_workers_std, df_factor_scores], axis=1)
# 因子得点だけを含むデータフレーム
df_factor_only = df_with_factor_scores.iloc[:, -fa_ml.n_factors:]
# データフレームをExcelファイルに保存
df_factor_only.to_excel("自分因子得点.xlsx", index=False)
print(df_factor_only)

# バイプロットの作図
score_ml = fa_ml.transform(df_workers_std)
coeff_ml = fa_ml.loadings_.T
fa1_ml = 0
fa2_ml = 1
labels_ml = df_workers.columns
annotations_ml = df_workers.index
xs_ml = score_ml[:, fa1_ml]
ys_ml = score_ml[:, fa2_ml]
n_ml = score_ml.shape[1]
scalex_ml = 1.0 / (xs_ml.max() - xs_ml.min())
scaley_ml = 1.0 / (ys_ml.max() - ys_ml.min())
X_ml = xs_ml * scalex_ml
Y_ml = ys_ml * scaley_ml
for i, label_ml in enumerate(annotations_ml):
    plt.annotate(label_ml, (X_ml[i], Y_ml[i]))
for j in range(coeff_ml.shape[1]):
    plt.arrow(0, 0, coeff_ml[fa1_ml, j], coeff_ml[fa2_ml, j], color='r', alpha=0.5, 
              head_width=0.03, head_length=0.015)
    plt.text(coeff_ml[fa1_ml, j] * 1.15, coeff_ml[fa2_ml, j] * 1.15, labels_ml[j], color='r', 
             ha='center', va='center')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("第１因子")
plt.ylabel("第２因子")
plt.grid()
plt.show()
