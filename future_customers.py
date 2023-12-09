# 初期の顧客数: 8000人
initial_customers = 8000
# 年間成長率: 20%
growth_rate = 0.2
# 期間: 3年
years = 3

# 3年後の顧客数を計算(複利成長を使用)
future_customers = initial_customers * ((1 + growth_rate) ** years)

# 英大文字26文字を使用して、生成可能なユニークなコードの数を計算する必要がある。
# 文字の数を指数とした数が、コードの総数になる。
num_digits = 1  # コードの桁数を1から始める。
num_characters = 26  # 英大文字は26文字。

# 生成可能なコードの総数が、3年後の顧客数以上になる最小の桁数を見つける。
while (num_characters**num_digits) < future_customers:
    num_digits += 1  # 条件を満たすまで桁数を1ずつ増やす。

# 最終的に求めた桁数と3年後の予測顧客数を出力する。
print(num_digits, future_customers)
