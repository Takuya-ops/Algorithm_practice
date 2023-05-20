from typing import List

def generate_primes_v1(numbers: int) -> List[int]:
  primes = []
  for x in range(2, numbers + 1):
    for y in range(2, x):
      
      if x % y == 0:
        break
    else:
      primes.append(x)
  return primes

if __name__ == "__main__":
  print(generate_primes_v1(50))