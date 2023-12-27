class Solution:
    def minCost(self, colors: str, neededTime: [int]) -> int:
        total_time = 0
        group_time = neededTime[0]  # Total removal time for the current group
        max_time_in_group = neededTime[0]  # Maximum removal time in the current group

        for i in range(1, len(colors)):
            # If the color is the same as the previous one, continue the group.
            if colors[i] == colors[i - 1]:
                group_time += neededTime[i]
                max_time_in_group = max(max_time_in_group, neededTime[i])
            else:
                # Color changed, add the time to remove the current group, except the most expensive one.
                total_time += group_time - max_time_in_group
                # Reset counters for the new group.
                group_time = neededTime[i]
                max_time_in_group = neededTime[i]

        # Add the last group's time to total_time.
        total_time += group_time - max_time_in_group
        return total_time


class Solution2:
    def minCost(self, solors: str, neededTime: [int]) -> int:
        total_time = 0
        group_time = neededTime[0]
        max_time_in_group = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                group_time += neededTime[i]
                max_time_in_group = max(max_time_in_group, neededTime[i])
            else:
                total_time += group_time - max_time_in_group
                group_time = neededTime[i]
                max_time_in_group = neededTime[i]
        total_time += group_time - max_time_in_group
        return total_time
