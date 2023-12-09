# -*- coding:utf-8 -*-
# 初期値の定義
initial_customers = 8000
annual_growth_rate = 20
years = 3

future_customers = initial_customers * ((1 + 0.01 * annual_growth_rate) ** 3)

num_digits = 1
num_alphabet_char = 26

while (num_alphabet_char**num_digits) < future_customers:
    num_digits += 1
    if num_alphabet_char**num_digits > future_customers:
        print("確保できる顧客管理数の最大値：" + str(num_alphabet_char**num_digits))


print("３年後の顧客：" + str(int(future_customers)), "\n必要な桁数：" + str(num_digits))
