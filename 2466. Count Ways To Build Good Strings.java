class Solution {
  public int countGoodStrings(int low, int high, int zero, int one) {
    // dp[i]を使って、長さiの良い文字列の数を記録する。
    int[] dp = new int[high + 1];
    dp[0] = 1;
    int mod = 1_000_000_007;

    // 各長さ `end` に対して反復処理する。
    for (int end = 1; end <= high; ++end) {
      // 0を0個、または1個追加して文字列を作ることができるかどうかをチェックする。
      if (end >= zero) {
        dp[end] += dp[end - zero];
      }
      if (end >= one) {
        dp[end] += dp[end - one];
      }
      dp[end] %= mod;
    }
    // 各有効長[low〜high]の文字列の数を合計する。
    int answer = 0;
    for (int i = low; i <= high; ++i) {
      answer += dp[i];
      answer %= mod;
    }
    return answer;
  }
}