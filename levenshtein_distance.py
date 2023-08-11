def levenshteinDistance(str1, str2):
    # 長い方の文字列を big に、短い方の文字列を sma に代入
    big = str1 if len(str1) > len(str2) else str2
    sma = str2 if big == str1 else str1

    # 初期化: prev_row と curr_row の作成
    prev_row = [k for k in range(len(sma) + 1)]  # sma の文字数分の初期値を持つリスト
    curr_row = [None for _ in range(len(sma) + 1)]  # 同様に None のリストを作成

    # ダイナミックプログラミングのループ: 大きな文字列を基準にループ
    for i in range(1, len(big) + 1):
        curr_row[0] = i  # 現在の行の最初の要素は i

        # サブループ: 小さな文字列に対してループ
        for j in range(1, len(sma) + 1):
            # 置換のコストを計算
            repl_cost = 0 if big[i - 1] == sma[j - 1] else 1

            # 最小コストの計算と代入
            curr_row[j] = min(
                prev_row[j] + 1,  # 挿入
                curr_row[j - 1] + 1,  # 削除
                prev_row[j - 1] + repl_cost,  # 置換 or 同一文字
            )

        # 行の切り替え: prev_row と curr_row を交換
        prev_row, curr_row = curr_row, prev_row

    # 最終的な Levenshtein 距離を返す（大きな文字列の終端の値）
    return prev_row[-1]


if __name__ == "__main__":
    str1 = "abc"
    str2 = "yabd"
    print(levenshteinDistance(str1, str2))
