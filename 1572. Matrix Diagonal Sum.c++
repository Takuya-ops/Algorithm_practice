class Solution
{
public:
  int diagonalSum(vector<vector<int>> &mat)
  {
    int n = mat.size();
    int ans = 0;

    for (int i = 0; i < n; i++)
    {
      // 一次対角線上の値を足し合わせる
      ans += mat[i][i];
      // 二次対角線上の値を足し合わせる
      ans += mat[n - 1 - i][i];
    }
    // 正方行列の次元が奇数の場合、中心の値が重複するため、取り除く
    if (n % 2 != 0)
    {
      ans -= mat[n / 2][n / 2];
    }
    return ans;
  }
};