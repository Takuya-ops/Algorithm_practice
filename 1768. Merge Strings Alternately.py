class Solution(object):
    def mergeAlternately(self, word1, word2):
        # 長さを取得
        m = len(word1)
        n = len(word2)
        # 初期化
        i = 0
        j = 0
        # 空のリスト
        result = []

        # 文字の長さ以下のとき
        while i < m or j < n:
            if i < m:
                # リストに対象の文字を加える
                result += word1[i]
                # 次の文字へ移動
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        # リスト形式で格納されているのでくっつける
        return "".join(result)
