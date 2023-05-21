# 関数に型明示ができるようにする
from typing import List, Generator

# 素数を抽出する関数（与えた数字までの素数を抽出する）
def generate_primes_v1(numbers: int) -> List[int]:
  # 空のリストの作成
  primes = []
  # for文を何回回したか
  i = 0
  for x in range(2, numbers + 1):
    for y in range(2, x):
      # for文カウント
      i += 1
      # 余りが０の時は含めない
      if x % y == 0:
        break
    else:
      # for文カウント
      i += 1
      primes.append(x)
  # for文を回した回数の表示
  print("v1=", i, "回")
  return primes

def generate_primes_v2(number: int) -> List[int]:
  primes = []
  # キャシュ用の辞書の作成
  cache = {}
  # for文のカウント用
  i = 0
  for x in range(2, number + 1):
    # for文の回数をカウントする
    i += 1
    is_prime = cache.get(x)
    if is_prime is False:
      continue
    primes.append(x)
    cache[x] = True
    # 倍数の除去
    for y in range(x*2, number+1, x):
      cache[y] = False
  print("v2", i, "回")
  return primes

# ジェネレータの場合
def generate_primes_v3(number: int) -> Generator[int, None, None]:
  cache = {}
  for x in range(2, number + 1):
    is_prime = cache.get(x)
    if is_prime is False:
      continue
    yield x
    cache[x] = True
    for y in range(x*2, number+1, x):
      cache[y] = False
    


if __name__ == "__main__":
  # 時間計測
  import time
  # 現時刻の取得
  start = time.time()
  # 関数の実行
  print(generate_primes_v1(50))
  # 処理にかかった時間
  print(time.time() - start)
  
  # 現時刻の取得
  start = time.time()
  # 関数の実行
  print(generate_primes_v2(50))
  # 処理にかかった時間
  print(time.time() - start)
  
  # 現時刻の取得
  start = time.time()
  # 関数の実行
  print([i for i in generate_primes_v3(50)])
  # 処理にかかった時間
  print(time.time() - start)
