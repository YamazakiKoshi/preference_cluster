import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルから固有値を読み込む
excel_file_path = "内訳固有値.xlsx"  # あなたのファイルパスに置き換えてください
df_eigenvalues = pd.read_excel(excel_file_path)

# 固有値を降順にソート
df_eigenvalues_sorted = df_eigenvalues.sort_values(by=df_eigenvalues.columns[0], ascending=False)

# スクリープロット
plt.figure(figsize=(10, 6))
plt.plot(df_eigenvalues_sorted.index + 1, df_eigenvalues_sorted[df_eigenvalues.columns[0]], marker='o', linestyle='-', color='b')
plt.title('スクリープロット')
plt.xlabel('因子の番号')
plt.ylabel('固有値')
plt.xticks(df_eigenvalues_sorted.index + 1)
plt.grid(True)
plt.show()

