# この問題を解くための一般的なアプローチは、文字の位置を記録し、同じ文字が再び出現したときにその間の距離を計算することです。

# 手順
# 文字の位置を記録する: 各文字の最後の位置を記録するための辞書を作成します。
# 最大距離を追跡する: 最大の距離を追跡し、その距離を更新します。
# 各文字について繰り返す: 文字列の各文字について繰り返し、文字が以前に現れたかどうかをチェックします。
# 距離の更新: 同じ文字が再び現れた場合は、その間の距離を計算し、最大値を更新します。


def maxLengthBetweenEqualCharacters(s):
    # 辞書を初期化して、文字の最後の位置を記録します。
    last_pos = {}
    max_length = -1

    # 文字列を通じて繰り返します。
    for i, char in enumerate(s):
        # 以前にこの文字が現れた場合、最大距離を更新します。
        if char in last_pos:
            max_length = max(max_length, i - last_pos[char] - 1)

        # 文字の位置を更新します。
        last_pos[char] = i

    return max_length


class Solution2:
    # 引数と返り値の型は？
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 辞書を作成
        last_pos = {}
        # 同じ文字が２回現れない場合は-1を返す
        max_length = -1
        # 位置（インデックス）と値を取得
        for i, char in enumerate(s):
            # 現在のイテレーションで扱っている文字が、辞書（lat_pos）に含まれているかを確認
            # 綴ミスlast_pos
            if char in lat_pos:
                max_length = max(max_length, i - last_pos[char] - 1)
            last_pos[char] = i
        return max_length


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_pos = {}
        max_length = -1

        for i, char in enumerate(s):
            if char in last_pos:
                max_length = max(max_length, i - last_pos[char] - 1)
            else:
                last_pos[char] = i

        return max_length


# Testing the function with a problematic string
sol = Solution()
test_str = "mgntdygtxrvxjnwksqhxuxtrv"
print(sol.maxLengthBetweenEqualCharacters(test_str))
