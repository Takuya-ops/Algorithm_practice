# 修正後の関数
def blackjackProbability(target, startingHand):
    cache = {}
    return blackjackProbabilityRecursive(target, startingHand, cache)


def blackjackProbabilityRecursive(target, startingHand, cache):
    if startingHand in cache:
        return cache[startingHand]
    if startingHand > target:
        return 1

    if target - 4 <= startingHand <= target:
        return 0


# テスト用
target_value = 20
initial_hand = 15  # 例: 初期手札が5と10のカードで合計15

result = blackjackProbability(target_value, initial_hand)
print(f"目標値 {target_value} に達する確率: {result}")
