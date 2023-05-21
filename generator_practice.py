# メモリの消費量の確認
import sys
# csvファイルをwith句で読み込む
import csv

# for i in range(10):
#   print(i)

# その都度計算する（ジェネレーター） → 大きなデータを扱う場合はジェネレータを使用するようにする（listは使用しない）
range_nums = range(10)
for i in range_nums:
  print(i)
  
# for i in [0,1,2,3,4,5,6,7,8,9]:
#   print(i)

# 数字すべてをメモリに置いている
list_nums = [0,1,2,3,4,5,6,7,8,9]
for i in list_nums:
  print(i)
  
# メモリサイズの確認
print("メモリサイズ:", sys.getsizeof(range_nums))
print("メモリサイズ:", sys.getsizeof(list_nums))

# csvファイルの読み込み
with open("example.csv") as f:
  reader = csv.DictReader(f)
  for line in reader:
    print(line)
    
# generator関数の自作（rangeを自作）
def myrange(stop):
  start = 0
  while start < stop:
    # 関数にジェネレータとしての役割を持たせる
    yield start
    start += 1
    
mr = myrange(10)
# print(type(mr))
# print(mr)
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
# ここでストップイテレーション
# print(next(mr))
# for i in mr:
#   print(i)
    
# 指定した数字から２までの偶数を返すイテレーター
from typing import List
def func(num: int) -> List[int]:
  numbers = []
  for i in range(num+1):
    if i%2 == 0:
      numbers.append(i)
    else:
      continue
  return numbers

if __name__ == "__main__":
  num = 20
  print(func(20))
  
# 与えられた数字までの偶数を逆順でリストに格納
def even(num):
  while num != 0:
    if num % 2 == 0:
      yield num
    num -= 1
    
print("======================")
print("=" * 22)
for i in even(10):
  print(i)
  

def even(num):
  while num != 0:
    if num % 2 == 0:
      yield num
    num -= 1


print("======================")
for i in even(10):
  print(i)
