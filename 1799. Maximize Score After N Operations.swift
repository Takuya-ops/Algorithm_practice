class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let maxStates = 1 << nums.count
        let finalMask = maxStates - 1

        var dp = [Int](repeating: 0, count: maxStates)

        for state in (0...finalMask).reversed() {
            guard state != finalMask else {
                dp[state] = 0
                continue
            }

            let numbersTaken = state.nonzeroBitCount
            let pairsFormed = numbersTaken / 2
            guard numbersTaken % 2 == 0 else {
                continue
            }

            for firstIndex in 0..<nums.count {
                for secondIndex in (firstIndex + 1)..<nums.count {
                    guard((state >> firstIndex) & 1 == 0), ((state >> secondIndex) & 1 == 0) else {
                        continue
                    }
                    let currentScore = (pairsFormed + 1) * gcd(nums[firstIndex], nums[secondIndex])
                    let stateAfterPickingCurrPair = state | (1 << firstIndex) | (1 << secondIndex)
                    let remainingScore = dp[stateAfterPickingCurrPair]
                    dp[state] = max(dp[state], currentScore + remainingScore)
                }
            }
        }
        return dp[0]
    }

    func gcd(_ a: Int, _ b: Int) -> Int {
        if b == 0{
            return a
        }
        return gcd(b, a % b)
    }
}