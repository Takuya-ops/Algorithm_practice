from typing import List

def counting_sort(numbers: List) -> List[int]:
  max_num = max(numbers)
  counts = [0] * (max_num + 1)
  result = [0] * len(numbers)
  
  for num in numbers:
    counts[num] += 1
  
  # 各数字の個数を調べる
  for i in range(1, len(counts)):
    counts[i] += counts[i-1]
  
  i = len(numbers) - 1
  while i >= 0:
    index = numbers[i]
    result[counts[index]-1] = numbers[i]
    counts[index] -= 1
    i -= 1
  return result
  
# テスト  
if __name__ == "__main__":
  nums = [4,3,6,2,7,1,6]
  print(counting_sort(nums))