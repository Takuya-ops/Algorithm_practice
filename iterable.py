# ジェネレータはイテレータの一種
# イテレータとは？：next()で回すことができてiter()関数でイテレータを返すもの。
# iter()関数でiteratorを返すものをiterableと呼ぶ。＝ iteratorもiterable
fruits = ["apple", "grape", "lemon"]


# print(next(fruits))
fruits_iterator = iter(fruits)

# print(iter(fruits))
print(next(fruits_iterator))
print(next(fruits_iterator))
# 自分自身を返しているかを確認
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))

# 自作のイテレーター
class MyIterator:
  def __init__(self, start=0):
    self.current = start
    
  def __next__(self):
    num = self.current
    self.current += 1
    return num
  
  def __iter__(self):
    return self
  
myiterator = MyIterator(10)
print(next(myiterator))
print(next(myiterator))

# 偶数を返すイテレータの作成
class EvenIterator:
  def __init__(self, start):
    self.current = start
  
  def __next__(self):
    # 数字が２未満の場合に処理を停止する
    if self.current < 2:
      raise StopIteration
    # 偶数の場合の処理
    elif self.current % 2 == 0:
      num = self.current
      self.current -= 2
      return num
    # 奇数の場合の処理
    else:
      self.current -= 1
      return self.__next__()
  
  def __iter__(self):
    return self

# テスト  
if __name__ == "__main__":
  even = EvenIterator(50)
  print(next(even))
  print(next(even))
  
# ジェネレータはイテレーターの一種
# ジェネレーターは関数で定義する（yieldを使う）
# イテレーターはクラスで定義する（yieldを使わない）
