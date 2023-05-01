class Solution
{
public:
  double average(vector<int> &salaries)
  {
    // 最高給与と最低給与
    int minSalary = INT_MAX;
    int maxSalary = INT_MIN;
    int sum = 0;

    for (int salary : salaries)
    {
      sum += salary;
      minSalary = min(minSalary, salary);
      maxSalary = max(maxSalary, salary);
    }
    return (double)(sum - minSalary - maxSalary) / (double)(salaries.size() - 2);
  }
};