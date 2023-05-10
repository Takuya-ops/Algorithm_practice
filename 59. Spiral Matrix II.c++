class Solution
{
public:
  vector<vector<int>> generateMatrix(int n)
  {
    vector<vector<int>> result(n, vector<int>(n));
    int cnt = 1;
    for (int layer = 0; layer < (n + 1) / 2; layer++)
    {
      // 方向１：左から右へのトラバース
      for (int ptr = layer; ptr < n - layer; ptr++)
      {
        result[layer][ptr] = cnt++;
      }
      // 方向２：上から下へのトラバース
      for (int ptr = layer + 1; ptr < n - layer; ptr++)
      {
        result[ptr][n - layer - 1] = cnt++;
      }
      // 方向３：右から左へのトラバース
      for (int ptr = n - layer - 2; ptr >= layer; ptr--)
      {
        result[n - layer - 1][ptr] = cnt++;
      }
      // 方向４：下から上へのトラバース
      for (int ptr = n - layer - 2; ptr > layer; ptr--)
      {
        result[ptr][layer] = cnt++;
      }
    }
    return result;
  }
};