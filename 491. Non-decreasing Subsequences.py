class Solution:
    # def findSubsequences(self, nums:　List[int]) -> List[List[int]]:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sequence = []

        def backtrack(index):
            if index == len(nums):
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return

            # nums[index]を追加した後もシーケンスが増加し続ける場合
            if not sequence or sequence[-1] <= nums[index]:
                # nums[index]をシーケンスに追加する
                sequence.append(nums[index])
                # 再帰的に呼び出す
                backtrack(index + 1)
                # シーケンスの末尾からnums[index]を削除
                sequence.pop()
            # 要素を追加せずに再帰的に呼び出す
            backtrack(index + 1)
        backtrack(0)
        return result
