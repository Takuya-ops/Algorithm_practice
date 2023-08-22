def laptopRentals(times):
    if len(times) == 0:
        return 0

    end_time = 0
    for elem in times:
        end_time = max(end_time, elem[1])

    dp = [0] * (end_time + 1)

    for time in times:
        for i in range(time[0], time[1]):
            dp[i] += 1

    return max(dp)
