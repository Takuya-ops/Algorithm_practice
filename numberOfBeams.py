from typing import List


class Solution:
    def numberOfBeams(self, bank: List[int]) -> int:
        prev_devices = 0
        total_beams = 0

        # iterate through each row in the bank
        for row in bank:
            # count the number of devices ('1's) in the current row
            curr_devices = row.count("1")

            # calculate beams only if there are devices in the current and previous row
            if curr_devices > 0 and prev_devices > 0:
                # for each pair of devices in different rows, there is one laser beam
                total_beams += prev_devices * curr_devices

            # update previous row's device count if current row is not empty
            if curr_devices > 0:
                prev_devices = curr_devices

        return total_beams


# Create an instance of the Solution class
sol = Solution()

# Example cases
print(sol.numberOfBeams(["011001", "000000", "010100", "001000"]))  # Expected output: 8
print(sol.numberOfBeams(["000", "111", "000"]))  # Expected output: 0
