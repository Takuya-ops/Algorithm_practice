list_a = [5, 6, 98, 3, 2, 4, 6, 4, 6, 3, 1, 0]

# 選択ソートで並び替えを行う
for i in range(len(list_a)):
    min_idx = i
    for j in range(min_idx+1, len(list_a)):
        if list_a[min_idx] > list_a[j]:
            min_idx = j
            list_a[i], list_a[j] = list_a[j], list_a[i]

print(list_a)

# ◎方針
# 左側の数字から順に、その右側にある数字を比較し、右側の数字のほうが小さければ入れ替える。

list_b = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(len(list_b)):
    min_idx = i
    for j in range(i+1, len(list_b)):
        if list_b[min_idx] > list_b[j]:
            list_b[min_idx], list_b[j] = list_b[j], list_b[min_idx]
            min_index = j

print(list_b)
