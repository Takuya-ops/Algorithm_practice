# -*- coding: latin-1 -*-
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(32):  # 32ビット整数の各ビットをチェック
            if n & mask:
                bits += 1
            mask <<= 1  # マスクを左に1ビットシフト
        return bits

    # テストケース


if __name__ == "__main__":
    test_cases = {
        "00000000000000000000000000001011": 3,
        "00000000000000000000000010000000": 1,
        "11111111111111111111111111111101": 31,
    }
    # テストコードの実行
    sol = Solution()
    results = {}
    for binary_str, expected in test_cases.items():
        n = int(binary_str, 2)  # 2進数文字列を整数に変換
        result = sol.hammingWeight(n)
        results[binary_str] = (result == expected, result)

    print(results)
