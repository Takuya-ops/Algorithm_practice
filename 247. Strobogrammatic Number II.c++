class Solution
{
public:
  vector<vector<char>> reversiblePairs = {
      {'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};

  vector<string> generateStroboNumbers(int n, int finalLength)
  {
    if (n == 0)
    {
      return {""};
    }
    if (n == 1)
    {
      return {"0", "1", "8"};
    }

    vector<string> prevStroboNums = generateStroboNumbers(n - 2, finalLength);
    vector<string> currStroboNums;

    for (string &prevStroboNum : prevStroboNums)
    {
      for (vector<char> &pair : reversiblePairs)
      {
        if (pair[0] != '0' || n != finalLength)
        {
          currStroboNums.push_back(pair[0] + prevStroboNum + pair[1]);
        }
      }
    }
    return currStroboNums;
  }
  vector<string> findStrobogrammatic(int n)
  {
    return generateStroboNumbers(n, n);
  }
};