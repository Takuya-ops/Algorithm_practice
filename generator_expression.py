# 使用メモリ量の算出
import sys

# リスト内包表記（処理＋for文）
square_list = [num * num for num in range(100)]
print(square_list)

# generator_expression
square_gen = (num * num for num in range(100))
# print(next(square_gen))
# print(next(square_gen))
# print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

# 偶数の２乗のみをリストに入れる
even_square = [num * num for num in range(100) if num % 2 == 0]
print(even_square)