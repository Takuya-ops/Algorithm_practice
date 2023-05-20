# 関数に型明示ができるようにする
from typing import List

# 素数を抽出する関数（与えた数字までの素数を抽出する）
def generate_primes_v1(numbers: int) -> List[int]:
  # 空のリストの作成
  primes = []
  for x in range(2, numbers + 1):
    for y in range(2, x):
      余りが０の時は含めない
      if x % y == 0:
        break
    else:
      primes.append(x)
  return primes

if __name__ == "__main__":
  print(generate_primes_v1(50))