from typing import List

def generate_prime(numbers: int) -> List[int]:
  prime = []
  for x in range(2, numbers + 1):
    for y in range(2, x):
      if x % y == 0:
        break
    else:
      prime.append(x)
  return prime

if __name__ == "__main__":
  print(generate_prime(2))