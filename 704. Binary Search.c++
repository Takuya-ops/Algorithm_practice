class Solution
{
public:
  int search(vector<int> &nums, int target)
  {
    int left = 0, right = int(nums.size()) - 1;

    while (left <= right)
    {
      // 中央インデックスと中間値を取得する
      int mid = left + (right - left) / 2;
      // 一致している場合（中間のインデックスと番号を取得）
      if (nums[mid] == target)
      {
        return mid;
      }
      // 小さい方の半分を破棄する
      else if (nums[mid] < target)
      {
        left = mid + 1;
      }
      // 大きい方の半分を破棄する
      else
      {
        right = mid - 1;
      }
    }
    // ターゲットが見つからなかった場合-1を返す
    return -1;
  }
};