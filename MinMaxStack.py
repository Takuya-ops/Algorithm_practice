class MinMaxStack:
    def __init__(self):
        self.maxes = []
        self.minis = []
        self.storage = []

    def peek(self):
        return self.storage[-1] if self.storage else None

    def pop(self):
        if self.storage:
            self.maxes.pop()
            self.minis.pop()
            return self.storage.pop()
        return None

    def push(self, number):
        if self.storage:
            self.maxes.append(max(number, self.maxes[-1]))
            self.minis.append(min(number, self.minis[-1]))
        else:
            self.maxes.append(number)
            self.minis.append(number)
        self.storage.append(number)

    def getMin(self):
        if self.storage:
            return self.minis[-1]
        return None

    def getMax(self):
        if self.storage:
            return self.maxes[-1]
        return None


# MinMaxStack クラスのインスタンスを作成
stack = MinMaxStack()

# 数値をスタックにプッシュ
stack.push(5)
stack.push(2)
stack.push(7)

# スタックの最小値と最大値を取得
print("最小値:", stack.getMin())  # 2 を出力
print("最大値:", stack.getMax())  # 7 を出力

# スタックから数値をポップ
stack.pop()

# スタックの最小値と最大値を再度取得
print("最小値:", stack.getMin())  # 2 を出力
print("最大値:", stack.getMax())  # 5 を出力

# スタックから数値をポップ
stack.pop()

# スタックの最小値と最大値を再度取得
print("最小値:", stack.getMin())  # 5 を出力
print("最大値:", stack.getMax())  # 5 を出力
