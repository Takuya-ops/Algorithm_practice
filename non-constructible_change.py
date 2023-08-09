def nonConstructibleChange(coins):
    # コインの額面を昇順にソートする
    coins.sort()

    # コインを使って作成できる最小のお金の額を表す変数を初期化
    minimum_change = 0

    # ソートされたコインのリストを順に走査
    for coin in coins:
        # 現在のコインの額面が、最小のお金の額に1を加えたものよりも大きい場合、ループを終了
        if coin > minimum_change + 1:
            break

        # 現在のコインの額面を最小のお金の額に加えることで更新
        minimum_change += coin

    # 最小のお金の額に1を加えた値を返す
    return minimum_change + 1


if __name__ == "__main__":
    coins = [6, 4, 5, 1, 1, 8, 9]
    print(nonConstructibleChange(coins))
