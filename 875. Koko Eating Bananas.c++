class Solution
{
public:
  int minEatingSpeed(vector<int> &piles, int h)
  {
    int speed = 1;

    while (true)
    {
      int hourSpent = 0;

      for (int pile : piles)
      {
        hourSpent += pile / speed + (pile % speed != 0);
        if (hourSpent > h)
        {
          break;
        }
      }
      if (hourSpent <= h)
      {
        return speed;
      }
      else
      {
        speed += 1;
      }
    }
  }
};